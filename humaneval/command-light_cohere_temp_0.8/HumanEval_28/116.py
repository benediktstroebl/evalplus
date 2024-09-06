```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> strings = ['a', 'b', 'ccc']
    >>> concatenate(strings)
    'abcccc'
    """
    return ''.join() + ''.join(strings)
```  This Python function, `concatenate`, takes a list of strings as an argument and concatenates them into a single string using the `+` operator and a list comprehension.