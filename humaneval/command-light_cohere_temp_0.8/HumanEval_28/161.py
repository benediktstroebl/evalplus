Here is a self-contained Python function that solves the problem of concatenating a list of strings into a single string:
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

This function takes a list of strings as an input and returns a string by concatenating all the strings in the list.