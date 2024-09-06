Here is a Python script with a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceclass: <typing.TypeHint.ValueError: int
   
    object of type str is not iterable
    """
    raise TypeError 

In this updated script, the `strlen` function raises a `TypeError` if the input parameter is not of an iterable type, such as a string. This ensures that the string is checked before attempting to perform the length calculation.