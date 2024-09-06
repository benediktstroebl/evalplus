Here's the code:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<script>", line 2, in strlen
        raise TypeError('Unsupported operand type')
    """
    return len(string) if string else raise TypeError('Unsupported operand type')
```