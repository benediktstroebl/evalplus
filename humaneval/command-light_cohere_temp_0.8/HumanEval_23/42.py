Certainly, here's a Python script with a self-contained function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen(' ')
    1
    >>> strlen('   ')
    2
    >>> strlen('  spaces')
    5
    >>> strlen('\\nOutput')
    4
    """
    return len(string)
```  This function uses the `len()` function built into Python strings to return the length of the given string.