```python
# Retrieve the requested function
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

This code defines a function called `concatenate` that takes a list of strings as input and returns a single string that concatenates all the inputs together. The function is tested with empty input and input list containing 'a', 'b', and 'c', and it successfully returns the expected output.