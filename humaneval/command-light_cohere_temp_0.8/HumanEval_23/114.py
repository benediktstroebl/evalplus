Here is a Python script that contains a self-contained function to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Tracebacks (None):
          ...
          File "<filename>", line 1, in strlen()
            raise TypeError("First argument must be str")
        """
    if not str:
        raise TypeError("First argument must be str")
    return len(string)
```