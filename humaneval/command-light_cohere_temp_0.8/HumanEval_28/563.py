Certainly! Here's the solution:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(s) for s in strings)
```  The function takes a list of strings as input and uses a list comprehension with the join() method to concatenate the strings into a single string.