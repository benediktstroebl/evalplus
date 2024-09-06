```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate
    Returns:
    str: Concatenated string
    """
    return ''.join(strings)

# Test the function
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate([]))  # Output: ''
print(concatenate(['a', ' ', 'b', 'c']))  # Output: 'abc'
print(concatenate(['a', 'b', 'c', 'd', 'e']))  # Output: 'bede'
```