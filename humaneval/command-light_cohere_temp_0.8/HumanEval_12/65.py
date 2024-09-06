```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string.
    Parameters:
    strings (list of str): list of strings.
    Returns the string of the longest one, or None if empty list.
    """
    = max(strings, key=len)
    return strings[1] if len(strings) == 1 else None

# tests
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = [''] * 3
print(longest(strings))  # Output: None

strings = ['a'] * 4
print(longest(strings))  # Output: 'a'

strings = ['abcd']
print(longest(['ab', 'ac', 'ad', 'bd']))  # Output: 'ac'
```