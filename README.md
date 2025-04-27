**# Email Validation API Testing**

This project tests the functionality of an Email Validation API using Python's `unittest` framework and `unittest.mock` for mocking external API calls (`requests.get`).

The function under test is:

```python
def fetch_email_validation(email):
    url = f"https://emailvalidation.abstractapi.com/v1/?api_key=YOUR_API_KEY&email={email}"
    response = requests.get(url)
    return response
```
**Test Case Name: test_successful_response**

* Description: 
Test if the API returns a valid deliverable email response.

Expected Result: Status code = 200, content contains "deliverability":"DELIVERABLE".

Test Case Name: test_failed_response

* Description:
Test if the API correctly handles an invalid/bad email response.

Expected Result: Status code = 400, content contains "error":"Invalid email".

**Validation Description**

**What is being validated?**

The HTTP response status code (200 or 400).

The content/body of the response for expected fields ("deliverability" or "error").

**Why this type of validation?**

Status code validation ensures that the API endpoint is behaving correctly: success for valid emails (200 OK), failure for invalid inputs (400 Bad Request).

Content validation ensures that the response body actually contains the correct information (such as the email deliverability status or an error message).

Mocking the API with unittest.mock is used to avoid real API calls, which makes the tests:

* Faster (no waiting for network responses),

* More reliable (tests don't fail if API server is down),

* Cost-effective (no API rate limits or charges),

* Isolated (unit tests should not depend on external systems).

**How to Run the Tests**

Install the dependencies if not already:
pip install requests

Run the tests:
python test_email_validation.py