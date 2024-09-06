Here's the self-contained Python script that solves the problem of calculating the length of a given string:
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
    File "{{ filename }}", line 16, in strlen()
        raise ValueError('Input string is empty')
    File "<stdin>", line 3, error=35
    ValueError: Input string is empty
    """
    if not string:
        raise ValueError('Input string is empty')
    return len(string)
```