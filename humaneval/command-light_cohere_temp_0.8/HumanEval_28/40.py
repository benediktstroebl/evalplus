Here is a self-contained Python function that solves the problem of concatenating lists of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc', ''])
    'abc'
    >>> concatenate(['a', 'bc', '', 'c'])
    'abc'
    """
    return ''.join(strings)
```
This function takes a list of strings as an argument and concatenates them into a single string, using the `join` method. It then returns the ingredients, using this method to create a string with all the elements.