Here's the self-contained Python script that solves the problem of concatenating lists of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([['a', 'b'], ['c', 'd']])
    ['aabbcd']
    """
    return ''.join(strings)
```
The function concatenate takes a list of strings as input and returns a single string by concatenating the strings in the list. This is easy to use, self-contained function can be used to quickly solve the problem of string concatenation in Markdown code blocks.