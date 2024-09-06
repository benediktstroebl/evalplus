```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') 
    Traceback (most recent call last):
      File "<ipythonfile>", line 4, in strlen()
        raise TypeError('unsupported operand type')
      File "<ipythonfile>", line 2: return __builtin__.strlen(string)
    TypeError: unsupported operand type(object) != str
    """
    return __builtin__.strlen(string)
```