Here's a self-contained Python function that concatenates strings in a list into a single string:
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
This code defines a function called `concatenate` that takes a list of strings as input and returns a concatenated string.  The method uses the same list and joins its elements using the `join` method to produce a new string that contains all the elements from the input list.