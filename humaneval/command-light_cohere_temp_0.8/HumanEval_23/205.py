Here is a self-contained Python function that calculates the length of any given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<stdin>", line position 10
    File "<string>.py", line 3
    AttributeError: 'str' object does not implement str.get()  

    expected from subclass of str'
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(string)
```