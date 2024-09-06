```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> strings = ['a', 'bcda', 'bc']
    >>> concatenate(strings)
    'abcdabc'
    """
    return ''.join("".join(strings))
```