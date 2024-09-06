```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc', ''])
    'abc'
    >>> concatenate(['abc'])
    'abc'
    >>> concatenate([123])
    Traceback (most recent call last):
      File "<ipythoninput[0]>", line 1, in <module>
        concatenate(...): ValueError: invalid literal for concatenation: '123'
    """
    result = ''.join(strings)
    return result
```