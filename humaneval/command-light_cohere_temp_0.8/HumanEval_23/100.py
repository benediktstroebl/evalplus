Here's a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen(' feeshi tEst ')
    10
    >>> strlen('') == 0
    True
    """
    return len(string)
```