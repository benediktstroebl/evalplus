```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
print(strlen('') == 0)   # Expected output: True
print(strlen('abc') == 3) # Expected output: True
```

In this script, the `strlen` function uses Python's built-in `len` function to calculate the length of the input string. The test cases at the end verify that the function behaves as expected. You can add more test cases as needed to ensure the function works correctly for different inputs.