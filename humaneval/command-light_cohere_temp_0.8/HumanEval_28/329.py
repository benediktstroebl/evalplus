```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join(strings)
```  This function takes a list of strings as input and returns a concatenated string by using list comprehension and the join() method.  The `return "".join(strings)` creates a new string that contains the concatenated values of the input strings.