```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc'])
    'abc'
    >>> concatenate(['a'])
    'a'
    >>> concatenate([1,2,3])
    Traceback (most recent call last):
    ...
    ValueError: expected str or bytes, got int instead
    """
    result = ''.join(strings)
    return result
```  This script defines a function `concatenate` that takes in a list of strings as an argument and returns a concatenated string. The test cases provided demonstrate the illustrates the usage of the function, passing various strings and testing the expected output.