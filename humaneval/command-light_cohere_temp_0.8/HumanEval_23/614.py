Here's the provided Python code with a self-contained function that calculates and returns the length of a given string:

```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') 
    Traceback (most recent call last):
    ...
    ValueError: why cannot convert string to int
    """
    return int(string)
```