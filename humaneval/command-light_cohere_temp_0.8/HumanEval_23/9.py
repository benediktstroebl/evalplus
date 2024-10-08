```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
    Traceback (most recent call last):
      File "<filename>", line 3, in <module>
        TypeError: 'str' object does not support item assignment
  """
    return len(string)
```