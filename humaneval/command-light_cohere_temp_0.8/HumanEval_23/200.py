Here is a Python script that defines a function `strlen` that computes the length of a given string:

```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abcde')
    5
    >>> len('')
    0
    """
    return len(string)
```