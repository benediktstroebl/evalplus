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
assert strlen('') == 0
assert strlen('abc') == 3
print("All test cases pass.")
```

This script defines the `strlen` function, which takes a string as input and returns its length. The function uses Python's built-in `len` function to calculate the length. The script also includes test cases to verify that the function behaves correctly for empty and non-empty strings.