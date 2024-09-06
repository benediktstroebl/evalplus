```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: integer number of characters in the string.
    Args:
        string: string to calculate the length
    Returns: integer
    Example:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      ...
    ValueError: unbound variable string
  """
    if not string:
        raise ValueError("Input cannot be empty")

    return len(string)
```