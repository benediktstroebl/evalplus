Here is a self-contained Python function that solves the problem of concatenating lists of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc'])
    'abc'
    """
    return ''.join(_ + ''.join(strings) if strings else '')
```

This function takes a list of strings as input and returns a string containing the concatenated strings. It uses the ** list comprehension and string concatenation to achieve this result.