```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc'])
    'abc'
    """
    return ''.join(strings)
```
This code provides a self-contained function `concatenate` which takes a list of strings and returns the concatenated string. The code passes all tests with different inputs and verifies that the output is as expected.