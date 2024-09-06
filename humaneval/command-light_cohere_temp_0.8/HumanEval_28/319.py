Here's the solution:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        concatenated string
    """
    return ''.join(strings)
```
We use the `join` function to concatenate a list of strings into a single string.