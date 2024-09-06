```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args: strings (List[str]): List of strings to concatenate
    Returns: str: Concatenated string
    """
    return ''.join(strings)

# Test the function with sample inputs
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: 'abc'
```