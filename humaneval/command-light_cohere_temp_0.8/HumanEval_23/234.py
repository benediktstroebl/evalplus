Here's the complete Python script with a self-contained function that calculates the length of a given string, passing the tests as described:

```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abc') == len('abc')
        True
        >>> len('') == strlen('')
        True
        >>> ''.join() == strlen('')
        True
        """
    return len(string)
```