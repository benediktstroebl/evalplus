Certainly! Here's a self-contained Python script with a function `strlen` that calculates the length of a given string:

```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<script>", line 1, in strlen
    ValueError: invalid literal for int() with base 10
    """
    return len(string)
```