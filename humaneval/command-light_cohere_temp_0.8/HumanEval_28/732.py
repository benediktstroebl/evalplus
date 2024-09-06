```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test case 1: empty list
print(concatenate([]))

# Test case 2: list of different strings
print(concatenate(['a', 'b', 'c']))

# Test case 3: nested list of strings
print(concatenate([['a', 'b'], ['c', 'd']]))
```