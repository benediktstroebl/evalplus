```python
def strlen(string: str) -> int:
    """ Return length of given string
    
    Args:
    string (str): Input string
    
    Returns:
    int: Length of the input string
    
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
    assert strlen('hello world') == 11
    print("All test cases pass")
```

This script defines the `strlen` function, which simply uses Python's built-in `len` function to return the length of the input string. The script also includes test cases to verify the correctness of the function. The `if __name__ == "__main__":` block ensures that the test cases are only run when the script is executed directly, not when it's imported as a module in another script.