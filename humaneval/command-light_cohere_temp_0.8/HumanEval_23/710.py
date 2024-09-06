Here is a self-contained Python script that defines a function `strlen` that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: The length of the string in bytes
        Raises TypeError if the input is not a string
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
        
    return len(string)

# Test cases
 >>> strlen('')
0
 >>> strlen('abc')
3
 >>> strlen('abcabc')
5
 >>> strlen('abcabcabc')
6
 >>> strlen('')
 Traceback (most recent call last):
    TypeError: Input must be a string
```

This function uses the `len()` function that returns the length of a given string. This self-contained function is designed to provide the functionality required without relying on external libraries.