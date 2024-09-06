```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join("".join(strings)
```
This code defines a function **concatenate** that takes a list of strings as input and returns the concatenated string. 

It achieves this by using the "join" function to combine the elements of the input list into a single string.