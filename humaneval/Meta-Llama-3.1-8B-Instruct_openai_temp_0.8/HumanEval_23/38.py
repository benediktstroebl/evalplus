```python
# strlen.py

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

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This Python script defines a function `strlen` that takes a string as input and returns its length. The `len` function is a built-in Python function that returns the number of items in an object, which in this case is a string. The script also includes docstrings and example use cases to demonstrate the function's behavior.