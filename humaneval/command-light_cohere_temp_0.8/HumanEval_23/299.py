Here is a self-contained Python script that defines a function `strlen` that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') 
    Traceback (most recent call last):
      File "<script>", line 9, in <module>
        strlen('') 
    ValueError: concatenate() arg must be str-like
    """
    return len(string)
```