```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type
    if type(a) is not type(b):
        return None
    # Check values
    if a == b:
        return None
    # Check string values
    if type(a) is str and type(b) is str:
        if a.find('.') > b.find('.'):
            return a
        elif a.find('.') < b.find('.'):
            return b
        elif a.find(',') > b.find(','):
            return a
        elif a.find(',') < b.find(','):
            return b
    # Check number values
    if type(a) is int and type(b) is int:
        return max(a, b)
    elif type(a) is float and type(b) is float:
        return max(a, b)
    elif type(a) is int and type(b) is float:
        return b
    elif type(a) is float and type(b) is int:
        return a
    else:
        return None

# Test cases
assertEqual(compare_one(1, 2.5), 2.5)
assertEqual(compare_one(1, "2,3"), "2,3")
assertEqual(compare_one("5,1", "6"), "6")
assertEqual(compare_one("1", 1), None)
```

The test suite includes 4 test cases that aim to validate the `compare_one` function. The first test case checks that the function correctly returns 2.5 when comparing 1 and 2.5. The second test case ensures that the function returns "2,3" when comparing 1 and "2,3". The third test case verifies that the function returns "6" when comparing "5,1" and "6". The fourth test case ensures that the function returns None when comparing 1 and 1. 

To run the test suite, you can use the Python test runner as follows:
```python
python -m unittest your_module.test_compare_one
```

Make sure to replace `your_module` with the actual module name where the test case is defined.