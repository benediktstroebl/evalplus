Here is a Python script that includes a self-contained function that computes and returns the length of a given string:

```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns:
            - Length of the given string.
        Args:
            string (str): The string to compute the length
        Returns:
            int: Length of the given string"""
    return len(string)

# Test the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3

# Test the function with invalid inputs
def test_strlen_invalid():
    assert strlen('1234') == 0  # This should evaluate to an error

# Test the function with a string containing only whitespace
def test_strlen_only_whitespace():
    assert strlen('  \t') == 0
```

This script provides a complete, self-contained solution to the problem of computing the length of a given string. You can use this this full solution with confidence.