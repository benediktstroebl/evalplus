### Self-Contained Python Script
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
if __name__ == "__main__":
    print(strlen(""))  # Expected output: 0
    print(strlen("abc"))  # Expected output: 3
```
This script defines a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to get the length of a string.

The `if __name__ == "__main__":` block is used to run the test cases when the script is run directly (not imported as a module). This allows us to verify that the function is working correctly.