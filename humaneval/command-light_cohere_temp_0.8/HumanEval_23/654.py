Certainly! Here's a self-contained Python script that defines a function `strlen` that calculates the length of a given string, as you requested:

```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
    ...
    TypeError: 'argument' 'string' should be str, not str
    """
    if not str(string):
        raise TypeError('"argument" "string" should be str, not str')
    return len(string)
```