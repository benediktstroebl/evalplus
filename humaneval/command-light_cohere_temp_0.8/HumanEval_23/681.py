Here's a Python script that defines a function strlen to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen(' ')
    1
    >>> strlen('   ')
    2
    >>> len('')
    0
    >>> len('') < 0
    False
    """
```