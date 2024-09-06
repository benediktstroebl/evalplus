```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return "".join("".join(strings))

# Test the function with sample inputs and verify the output
strings = ["a", "b", "c"]
result = concatenate(strings)
assert result == "abc"
```