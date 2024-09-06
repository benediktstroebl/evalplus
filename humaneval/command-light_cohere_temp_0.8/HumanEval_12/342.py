```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    Parameters:
    strings: list of strings

    Returns:
    string, or None if the list is empty or has the same length
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test the function
longest(['a', 'bb', 'ccc']) # Output: 'ccc'
longest(['a', 'bc', 'bb']) # Output: 'a'
longest([]) # Output: None
```
The function takes a list of strings as input and returns the longest string from the list. If the list is empty or has the same length, the function returns None.