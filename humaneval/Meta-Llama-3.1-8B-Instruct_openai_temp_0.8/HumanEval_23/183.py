```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    Args:
        string (str): The input string
    
    Returns:
        int: The length of the string
    
    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test the function
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

In this script, we use the built-in `len()` function in Python to calculate the length of the string. This function is already implemented in the Python standard library, so there is no need to implement it manually. The `len()` function is the most efficient way to get the length of a string in Python. 

However, I have still implemented it for practice and understanding purposes.