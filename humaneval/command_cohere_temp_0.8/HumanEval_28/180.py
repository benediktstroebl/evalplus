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

The function `concatenate` takes a list of strings as an argument and returns a single string that concatenates all the strings in the list. The example usage and test cases provided are also included.