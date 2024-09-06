Here's a self-contained Python function that solves the problem of concatenating lists of strings into a single string:
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
The `concatenate` function takes a list of strings as input and returns a concatenated string. It uses the the` join` to build the string by iterating through the input list of strings and joining them with the `join` string.