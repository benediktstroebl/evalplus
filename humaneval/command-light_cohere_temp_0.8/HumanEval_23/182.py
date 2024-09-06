Here is a self-contained Python script that defines a function `strlen` which calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('weekend')
    5
    >>> len('')
    0
    >>> input = 'Beep Beep'
    >>> strlen(input)
    5
    """
    return len(string)
```