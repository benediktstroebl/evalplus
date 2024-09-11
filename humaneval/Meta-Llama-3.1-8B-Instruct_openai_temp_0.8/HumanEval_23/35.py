```python
def strlen(string: str) -> int:
    """ Return length of given string
    
    Args:
        string (str): The input string.
    
    Returns:
        int: The length of the string.
    
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

This script defines a `strlen` function that returns the length of a given string. It uses the built-in `len` function in Python, which returns the number of items in an object. The function is then tested with two example inputs. 

Note that in Python, the function name `strlen` is not necessary as `len` function is already available and it is more Pythonic to use `len` instead of `strlen`. However, I have provided the function as per the given specification.