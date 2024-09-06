Here is a self-contained Python function that solves the problem of joining a list of strings into a single string:
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
This function takes a list of strings as input and uses the `join` method to concatenate them into a single string.