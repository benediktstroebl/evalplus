Here is a Python script with a self-contained function that solves the problem of concatenating list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b'])
    'ab'
    >>> concatenate(['a', 'b', 'c', 'd'])
    'adc'
    """
    return ''.join(*strings)
```
This script defines a function called `concatenate` that takes in a list of strings and returns a single concatenated string. The function uses the use of a list comprehension to create the string from the input list of strings.