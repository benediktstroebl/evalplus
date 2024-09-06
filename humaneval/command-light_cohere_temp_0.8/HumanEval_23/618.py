Here is a Python script with a self-contained function that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string
    """
    return len(string)

# Test case 1:
assertEqual(strlen(''), 0)

# Test case 2:
assertEqual(strlen('abc'), 3)

# Test case 3:
assertEqual(strlen('  cee')), 5)
```
The provided code defines a function `strlen` that calculates the length of a given string. The function utilizes the string's `len` method to determine its length. The code also includes three test cases to verify the correctness of the `strlen` function:

Test Case 1: Length of an empty string ('') should return 0, as empty strings have a length of 0.

Test Case 2: Length of 'abc' should return 3, as 'abc' has 3 characters.

Test Case 3: Length of multiple spaces ('  cee') should return 5, as there are 5 characters in '  cee'.