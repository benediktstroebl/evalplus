```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Find the length of the longest string.
    Args:
        strings: list of strings.
    Returns: the first string with the maximum length.
    """
    None if empty list.
    """
Longest string is None
    """
    if not strings:
        return None
    # use max to find the longest string
    max_length = max(len(str) for str in strings)
    # create the result string by joining the strings
    result = ''.join(strings[i:i+max_length] for i, max_length in zip(range(len(strings)), (max_length, 1)))
    return result
```