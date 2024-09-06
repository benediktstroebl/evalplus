Here's a self-contained Python function that concatenates a list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string and return it.
    Args:
        strings (list of strings)
    Returns:
        concatenated string
    """
    return ''.join(strings)
```

This function takes a list of strings as an argument and returns a concatenated string by using the `join` method with the list of strings.