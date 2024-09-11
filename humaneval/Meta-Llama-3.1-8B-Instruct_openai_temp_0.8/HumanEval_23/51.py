```python
def strlen(string: str) -> int:
    """ Return length of given string
    
    Args:
        string (str): The input string for which the length is to be found
    
    Returns:
        int: The length of the input string
    
    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```

You can run this script in any Python environment to test the function. The `len` function in Python is used to find the length of a string, list, tuple, dictionary, etc. This script simply wraps that function in a more descriptive and reusable function called `strlen`.