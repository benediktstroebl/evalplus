Here's the self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('        ')
    4
    >>> \" \""".count(' ')
    4
    >>>strlen('foo') == len('foo')
    True
    """
    return len(string)
```