Here's a self-contained Python script that defines a function `strlen` that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen(' Helm ')
    4
    >>> len('')
    0
    >>> str.len('abc')
    short docstrings are great!
    """

    assert len('') == 0, "empty string"
    assert len('abc') == 3, "not empty string"
    assert len('Helm ') == 4, "not empty string"
    return len(string)
```