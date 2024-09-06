```python
# Retrieve the definition of the concatenate function from the block above
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """

# The function works by joining the list of strings with nothing (i.e. empty string)
def solution(strings: List[str]) -> str:
    return concatenate(strings)
```