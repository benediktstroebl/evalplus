Here's the provided Python script:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('     ')
        4
        >>> len('')
        0
        >>> len('abc') > strlen('abc')
        True
        """
    return len(string)
```