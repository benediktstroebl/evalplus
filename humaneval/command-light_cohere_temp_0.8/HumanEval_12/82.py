```python
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    or None if empty. """
    - if not strings:
        return None
    max_length = max(len(string) for string in strings)
    return max(strings)[0] if max_length == len(strings) else None
```
Do you have any other Python or coding related questions?