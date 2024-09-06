Here's a self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('hello world')
    11
    >>> strlen('') == 0
    True
    """
    return len(string)
```