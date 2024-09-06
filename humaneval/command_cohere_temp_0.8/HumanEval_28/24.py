```python
# Retrieve the requested script
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    for string in strings:
        result += string
    return result
```

This code defines a function called `concatenate` that takes in a list of strings and returns a single string that concatenates all the strings in the list. The function is tested with empty and non-empty lists and returns the expected results.