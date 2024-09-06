Here is a self-contained Python script that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Testing the function with known strings
test_strlen = str.test_strlen("") == 0
test_strlen("abc") == 3
test_strlen("hello world!") == 13
test_strlen(" ") == 0
```
This script defines a function `strlen` that calculates the length of a given string, and then provides test cases to ensure the function's correctness.  The output of running this code will display the error messages for the provided inputs that do not match the expected results.