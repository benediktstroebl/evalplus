```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc'])
    'abc'
    >>> concatenate(['a', 'b'])
    'ab'
    >>> concatenate(['ab', 'c'])
    'abc'
    """
    return ''.join(*strings)
```  This code defines a function called **concatenate** that takes in a list of strings as an argument. The function then uses the * string product built-in function **join()** to concatenate all the strings in the list into a single string.