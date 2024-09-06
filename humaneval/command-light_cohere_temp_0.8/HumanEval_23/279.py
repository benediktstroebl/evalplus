Here's a self-contained Python function that calculates the length of any given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abc 123')
    5
    >>> strlen('') == 0
    True
    """
    return len(string)
```  This function returns the length of the given string, which is a common operation performed in many string manipulation tasks.