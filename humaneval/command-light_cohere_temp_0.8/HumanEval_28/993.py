Certainly! This script defines a function called `concatenate` which takes a list of strings and returns a concatenated string. The function uses the string interpolation to combine the strings into a single string, with an empty string as a separator. 

Here's the code:
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