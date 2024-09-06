Here's the solution that is self-contained and passes all the tests:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    0
    """
    return len(string)
```  This code defines a function `strlen` which takes a string as an argument and returns its length.  It is uses the string's `len` built-in function to get its length.