Here's a self-contained Python function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('123')
    3
    >>> strlen('') == 0
    True
    """
    return len(string)
```  This function takes a string as input and returns its length, passing all test cases without requiring external functions or imports.