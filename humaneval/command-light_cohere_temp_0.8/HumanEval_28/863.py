Certainly! Below is a self-contained Python function that concatenates strings within a list:
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
```
This function uses the `join()` method to join the strings in the list into a single string.