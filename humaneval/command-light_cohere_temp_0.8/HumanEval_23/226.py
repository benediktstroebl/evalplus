```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Tracebacks (None): 
            File "<string>", line 3, in strlen()
                raise ValueError('" "' + s + '" expected string')
            File "<string>", line 6, in __main__

    """
    if not string:  # empty string
        return 0
    try:
        return len(string)
    except ValueError as e:
        raise ValueError(str(e) + f' expected string, got {type(string)}')
```