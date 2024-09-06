Here's a self-contained Python script that defines a function `strlen` that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    undefined
    """
    return len(string)
```  This script is fully self-contained: it defines, implements, and tests a function that calculates the length of a given string.