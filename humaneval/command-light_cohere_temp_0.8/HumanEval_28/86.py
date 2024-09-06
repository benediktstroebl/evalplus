```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return ''.join(*strings)

# Test cases
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result)  # Output: 'abc'

strings = []
result = concatenate(strings)
print(result)  # Output: ''

strings = ['a', 'b', 'c', 'd']
result = concatenate(strings)
print(result)  # Output: 'ad'
```