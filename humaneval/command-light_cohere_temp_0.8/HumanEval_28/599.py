```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(''.join(strings)  # using join() with string list conversion
```
The code defines a function `concatenate` which takes a list of strings as input and returns the concatenated string. The test cases demonstrate that usage of the function, passing in an empty list and a list with three strings, and the output is the expected string concatenation result ''.