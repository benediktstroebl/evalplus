Certainly! Here's a self-contained Python script that defines a function `strlen` solving the length of a given string in markdown:

```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('   ')
    4
    >>> strlen('   1234')
    4
    """
    return len(string)
```