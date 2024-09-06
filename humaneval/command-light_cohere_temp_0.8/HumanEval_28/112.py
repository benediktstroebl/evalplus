Here is a self-contained Python function that solves the problem of joining a list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['']) [''] # String, empty string
    >>> concatenate([['a', 'b'], ['c', 'd']]) ['abcd']
    """
    return ''.join(strings)
```
This function takes a list of strings as input and returns a string containing the concatenated strings. The `<<>` operator is used to concatenate the strings, which is the standard Python operator for list concatenation. The result is exactly as expected, and the code is self-contained.