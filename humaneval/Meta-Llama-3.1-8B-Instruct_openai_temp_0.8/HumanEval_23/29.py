```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    Args:
        string (str): Input string
    
    Returns:
        int: Length of the string
    
    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)


if __name__ == "__main__":
    # Test cases
    print(strlen(""))  # Expected output: 0
    print(strlen("abc"))  # Expected output: 3
```

In this script:

1. We define the `strlen` function that takes a string as input.
2. The `len` function is used to get the length of the string.
3. We include docstrings to provide documentation for the function, including descriptions, parameters, return values, and examples.
4. In the `if __name__ == "__main__":` block, we include test cases to verify the function works correctly.