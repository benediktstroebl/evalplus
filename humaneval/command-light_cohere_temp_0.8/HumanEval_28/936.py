Here's the function `concat` which takes a list of strings and returns the concatenated string:

```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    if not strings:
        return ""
    return ''.join(''.join(strings))
```

You can test the function with different inputs and verify the expected output.