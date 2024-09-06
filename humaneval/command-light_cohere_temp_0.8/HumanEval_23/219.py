Here is a self-contained Python script that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
   sale
    Traceback (most recent call last):
      File "<stdin>", line, line number 2
        AttributeError: 'str' object does not support attribute __sizeof__'
    """
    return len(string)
```