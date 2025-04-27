import unittest
from unittest.mock import patch, Mock
import requests

# Function to test
def fetch_email_validation(email):
    url = f"https://emailvalidation.abstractapi.com/v1/?api_key=e3c64ba0c6d94807bfe58ef0eecc2452&email={email}"
    response = requests.get(url)
    print(response.status_code)
    print(response.content)
    return response

# Test case class
class TestEmailValidationAPI(unittest.TestCase):

    @patch('requests.get')
    def test_successful_response(self, mock_get):
        # Mock the response object
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'{"deliverability":"DELIVERABLE","quality_score":"0.95"}'

        mock_get.return_value = mock_response

        # Call the function
        response = fetch_email_validation("ahmadnehal258@gmail.com")

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"deliverability":"DELIVERABLE"', response.content)

    @patch('requests.get')
    def test_failed_response(self, mock_get):
        # Simulate a bad response (e.g. bad request or wrong email)
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.content = b'{"error":"Invalid email"}'

        mock_get.return_value = mock_response

        # Call the function
        response = fetch_email_validation("bademail")

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'"error":"Invalid email"', response.content)

if __name__ == '__main__':
    unittest.main()
