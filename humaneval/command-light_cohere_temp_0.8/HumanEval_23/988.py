Here is a Python script that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string
    """
    return len(string)

# Test case 1: empty string
assert strlen('') == 0

# Test case 2: one-character string
assert strlen('abc') == 3
```

This code defines a `strlen` function that calculates the length of the given string using the `len()` function. The `assert` statements are used to verify that the function is working correctly for the given test cases.