Here's the self-contained Python script with a function `strlen` that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abc bytes')
    5
    >>> strlen('') == 0
    True
    """
    return len(string)
```