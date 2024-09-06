```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, returns the longest one or None if empty.
    Args:
        strings: list of strings
    Returns:
        The longest string or None.
    """
    strings = [string.join(strings) if len(strings) > 0] else None
    return max(strings, key=len)
```
This function takes a list of strings as an input and returns the longest string in the list. The function first converts the strings into a list of characters and then uses the max function with the key set to return the longest character.