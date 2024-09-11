```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test the function
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All tests passed.")
```
This script defines the `strlen` function, which uses the built-in `len` function to return the length of the input string. The function includes a docstring that describes its purpose, arguments, return value, and provides example usage. The script also includes tests to verify the function's correctness.