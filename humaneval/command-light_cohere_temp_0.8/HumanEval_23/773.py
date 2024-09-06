```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<input>", line 1, in strlen
        ^
    AssertionError: UnionError: Length must not exceed str.string max_items(array)' 
    """ 
    return len(string)
```