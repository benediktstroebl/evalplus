```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> strings = ['a', 'bb', 'ccc']
    >>> concatenate(strings)
    'aabbccc'
    """
    if not strings:
        return ""
    return "".join("".join(strings)
```
The above-given function 'concatenate' takes a list of strings as an input and returns the concatenated string. It first checks if the interested list is empty, in which case it returns an empty string. Otherwise, it joins the strings using the "+" operator and returns the joined result.