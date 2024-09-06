```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
```

This code defines a function called `concatenate` that takes a list of strings as input and returns a concatenated string. The code implements this using a list comprehension to join the strings with the `join` operator.