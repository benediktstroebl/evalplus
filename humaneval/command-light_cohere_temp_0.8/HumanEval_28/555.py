Here is a self-contained Python function that solves the problem you described: 
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
This function takes a list of strings as an argument and returns a single string by concatenating the strings together. 

The function uses the string method 'join' to concatenate the strings in the list into a single string, and returns the result.