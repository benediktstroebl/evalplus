```python
def strlen(string: str) -> int:
    """
    Return length of given string.

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
    print(strlen(""))  # Expected output: 0
    print(strlen("abc"))  # Expected output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function to calculate the length of the string. The `if __name__ == "__main__":` block is used to test the function. When the script is run directly, this block is executed and the function is tested with two example inputs.