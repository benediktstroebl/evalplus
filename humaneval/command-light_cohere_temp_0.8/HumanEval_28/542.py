Here is a self-contained Python function that solves the problem of concatenating list of strings into a single string, and passes the tests:
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
This function takes a list of strings as input and returns a string containing the concatenation of all the strings in the list.