```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test cases
strings = ['a', 'bcde', 'test', 'good']
print(concatenate(strings))  # Output: goodtcdeestg
strings = []
print(concatenate(strings))  # Output: 

strings = ['a', 'bcde']
print(concatenate(strings))  # Output: abcde
```