Here is a self-contained Python function that solves the problem of concatenating list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string and return it.
    :param strings: List of strings to be concatenated
    :return: Concatenated string
    """
    return ''.join(strings)
```

This function takes a list of strings as an argument and returns the concatenated string by using the `join` method on a string.