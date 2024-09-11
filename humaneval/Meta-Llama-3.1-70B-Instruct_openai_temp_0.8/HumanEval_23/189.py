```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
    string (str): Input string.

    Returns:
    int: Length of the input string.

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

This script defines a function `strlen` that uses the built-in `len` function to calculate the length of a given string. It includes a docstring that describes the function's behavior, its arguments, and its return value, along with examples that demonstrate how to use it.

The script also includes test cases that verify the function's correctness. The `if __name__ == "__main__":` block is used to ensure that the test cases only run when the script is executed directly, not when it's imported as a module in another script.