Here's the self-contained Python script that defines a function `strlen` that computes the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen(' bar') 
    4
    >>> strlen('') == 0
    True
    """
    return len(string)
```