```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
```  This script defines a function `concatenate` that takes a list of strings as input and returns a concatenated string.  The using the strings in the list, the function uses the `join` function to concatenate all the strings into a single string and then returns the result.