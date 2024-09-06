```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b', 'bc'])
    'abc'
    >>> concatenate(['a', 'bc', 'b'])
    'abbc'
    >>> concatenate(['a', 'bc', 'bb'])
    Traceback (most recent call last):
      File "example.py", line 21, [Err]
    """
    if not strings:
        return ""
    return "".join(*strings)
```