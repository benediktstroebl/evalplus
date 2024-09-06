```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
```  This code defines a function called concatenate that takes a list of strings as an input and returns a string by concatenating all the strings in the list.

The function uses the join() method which is equivalent to using ''.join(strings) and returns the concatenated string as the output.