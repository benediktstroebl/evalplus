Here's the solution:

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

This function concatenates a list of strings into a single string, following the format of the original problem. The function is self-contained and only operates on the parameters passed to its function. It also has built-in to pass all the tests.