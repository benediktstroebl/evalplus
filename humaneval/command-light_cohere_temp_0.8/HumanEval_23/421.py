Here is a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abc') == 3
    True
    >>> input = 'hello world'
    >>> len(input)
    13
    """
    return len(string)
```