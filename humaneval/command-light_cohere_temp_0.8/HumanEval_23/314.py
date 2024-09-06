Here is a self-contained Python function that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abc 123')
    5
    >>> strlen(' foo bar ')
    7
    """
    return len(string)
```  This function takes a string as input and returns its length as an integer.  It uses the would implementation, which is efficient and widely used.