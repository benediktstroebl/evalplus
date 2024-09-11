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

# Test cases
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases pass")
```

This script defines the `strlen` function, which uses the built-in `len` function to calculate the length of a given string. The function includes a docstring with a description, arguments, return value, and examples.

The script also includes two test cases to verify that the function works as expected. If the function passes all test cases, it prints "All test cases pass".