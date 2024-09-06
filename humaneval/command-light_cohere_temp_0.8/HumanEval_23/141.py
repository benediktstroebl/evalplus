Here is a Python script that contains a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('  ')
    4
    >>> strlen('hello world!  # will give error: invalid literal for indentation
    """
    return len(string)
```