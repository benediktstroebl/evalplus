```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test cases
print(strlen('') == 0)  # Expected output: True
print(strlen('abc') == 3)  # Expected output: True
```
This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python to calculate the length of the string.

Note that the test cases at the end of the script are not technically necessary for the function to work, but they can be helpful for verifying that the function is working correctly.