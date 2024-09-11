```python
def strlen(string: str) -> int:
    """
    Return length of given string.
    
    Args:
        string (str): Input string
    
    Returns:
        int: Length of the input string
    """
    # Using built-in len() function to calculate the length of the string
    return len(string)


# Testing the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The length is calculated using the built-in `len()` function in Python. The script also includes docstrings to provide documentation for the function and test cases to verify its correctness.