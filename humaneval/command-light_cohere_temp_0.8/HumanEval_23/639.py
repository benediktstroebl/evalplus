Here is a self-contained Python script with a function that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('arg') 
    Traceback (most recent call last):
      File "<filename>", line 1, in 'strlen'
        TypeError: 'arg' object does not support attribute 'str'
999")
    """
    return len(string)
```