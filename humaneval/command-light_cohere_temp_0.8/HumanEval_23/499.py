Here is a self-contained Python script that defines a function `strlen` that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abc instructions')
    3
    >>> strlen('') == 0
    True
    >>> str.join(''.join(x'a', 'bc', 'cd'))
    5
    """
    return len(string)
```  This script provides a function to calculate string length using Python's built-in `len()` function.