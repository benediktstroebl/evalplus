Here's the self-contained Python function that solves the problem:
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Parameters:
    strings: List of str
    Returns: concatenated string
    """
    return ''.join(strings)
```
The function concatenate takes a list of strings and returns the concatenated string. It uses the basic .join method to join the strings in the list into a single string.