Here's the self-contained Python script that defines a function `strlen` which calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<stdin>", line position 8
        AttributeError: 'str' object does not attribute __str__'
    """
    return len(string)
```