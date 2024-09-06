```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<script>", line 1, in <module>:\str_len\(string)\^ 
           ^ --> ValueError: invalid literal for int() with base 10: ''
    >>> strlen(' punct')
    4
    """
    return len(string)
```