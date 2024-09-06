Here's the self-contained Python script with a function that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') == 0
    True
    >>> strlen('sentence') == 7
    True
    >>> str.join('hello world') == strlen('hello world')
    True
    """
    return len(string)
```