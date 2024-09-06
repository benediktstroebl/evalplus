```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') 
    Traceback (most recent call last):
      File "<string>", line 6, in strlen
        str.count()
    string = ''  [Exception occurred: peoplescript]
    """
    return len(string)
```