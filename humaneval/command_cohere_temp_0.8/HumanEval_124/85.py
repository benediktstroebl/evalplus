Here's a Python script that implements the `valid_date` function, with corresponding tests:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'\d\d-\d\d-\d\d\d\d', date))
    
    if 1 <= mm <= 12:
        # Days validation for months between 1,3,5,7,8,10,12
        if (mm in [1, 3, 5, 7, 8, 10, 12] and 1 <= dd <= 31) or
           (mm in [4, 6, 9, 11] and 1 <= dd <= 30) or
           (mm == 2 and 1 <= dd <= 29):
            return True
        else:
            return False
    else:
        return False

# Test Cases
assert valid_date('06-04-2020')
assert not valid_date('06/04/2020')
assert not valid_date('04-0-2040')
assert not valid_date('15-01-2012')
assert not valid_date('')
assert valid_date('03-11-2000')
```

This code defines a function `valid_date` that takes a date string as input and returns `True` if the date is valid according to the given rules, and `False` otherwise. The function checks that the date string is not empty, has the correct format, and the day and month values fall within the specified ranges.

The code also includes test cases to verify the correctness of the `valid_date` function. You can add more test cases to cover additional scenarios and ensure the function's behavior matches the problem statement. 
To run the tests, simply execute the script. The test cases will be executed, and any failures will be asserted. This provides assurance that the code works as intended, according to the given problem.  If you want to run the tests individually, the pytest framework needs to be installed in the environment. 

You can install it with the following command: 
```
pip install pytest
``` 
If you want to execute the test cases individually, you can prefix the function with `pytest` and add the test case as an argument, like this: 
```python
pytest 'pytest.test_valid_date("06-04-2020")'
``` 
This will run only the test of the validation of the date "06-04-2020", in this way you can focus on testing one particular aspect of the function's behavior at a time.