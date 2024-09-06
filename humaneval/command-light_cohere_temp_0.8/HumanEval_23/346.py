Here is a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen(' grazed Bearded Hare ')" 
    29
    >>> strlen('  <= 32   ')
    32
    """
    return len(string)
```