Here's the improved version of the script with a self-contained function that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen(' ')
    2
    >>> strlen('')
    0
    >>> "hello" != "
    True
    """
    return len(string)
```