Here is a Python script that contains a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<input>", line 1, in <module>:\strlen\(\)
    ValueError: empty string cannot evaluate to integer
    """
    if not string:
        raise ValueError("empty string cannot evaluate to integer")
    return len(string)
```