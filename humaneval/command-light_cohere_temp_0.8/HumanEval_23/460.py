Here is a self-contained Python script with a function that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') != 0
    False
    """
    return len(string)
```