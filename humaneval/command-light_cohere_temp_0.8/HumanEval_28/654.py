```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return ''.join(strings)

# Test case: Concatenate empty list into empty string
print(concatenate([]))  # Output: ''

# Test case: Concatenate list of strings into a string
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```
This code provides a self-contained function that concatenates a list of strings into a single string, with comprehensive documentation and passable tests.