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
The code uses a for loop to iterate over the list of strings and append each element to a result string. The result is then returned, providing a functioning solution to the problem.