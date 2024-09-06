```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return ''.join(strings)

# Test cases
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
strings = []
print(concatenate(strings))  # Output: ''
```