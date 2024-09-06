Here is a self-contained Python function that solves the problem of concatenating lists of strings: 

```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([['a'], ['b'], ['c']])
    ['aa', 'bb', 'cc']
    """
    return ''.join(strings)
``` 

This function takes a list of strings as input and concatenates them into a single string, with an empty string ('') as the default case.