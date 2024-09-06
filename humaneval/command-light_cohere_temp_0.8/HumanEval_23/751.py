Here is a self-contained Python function that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('hello world')
    11
    >>> strlen('')
    <__main__.strlen object at 0x>
    """
    return len(string)
```