Here's a self-contained Python function that solves the problem of concatenating a list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([['a'], ['b'], ['c']])
    ['aa', 'bb', 'cc']
    """
    return ''.join(''.join(strings)
```
This function takes a list of strings as input and returns a new string concatenated with the elements of the input list. The function uses the  a method that concatenates the strings in the list using the join() method and converts the result to a single string using the join('.') method.