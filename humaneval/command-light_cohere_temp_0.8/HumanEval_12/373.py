```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in the list.
    Args:
    strings (List[str]): A list of strings.
    Returns: the longest string, or None if empty list.
    """
    longest([]) --> None
    longest(['a', 'bb', 'ccc']) --> 'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)

# Tests
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest(['a', 'bb', 'aaa'])))  # Output: 'aaa'
print(longest([]))  # Output: None
```