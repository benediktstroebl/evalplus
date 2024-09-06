Certainly, here's a self-contained Python script that defines a function `strlen` that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('illage')
        5
        """
    return len(string)
```