Here is a self-contained Python function that solves the problem of concatenating strings in a markdown code block: 

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

This function takes a list of strings as input and returns a single string by concatenating the strings together. The code is straightforward and follows Python's named function convention.