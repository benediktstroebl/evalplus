```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<ipythoninput>", line 1, in strlen
    ValueError: Input string must be str type
    """
    assert isinstance(string, str), 'Input string must be str type'
    return len(string)
```