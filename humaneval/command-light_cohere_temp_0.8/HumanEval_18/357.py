```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, taking overlapping matches into account. 
    """
    string: str - The original text
    substring: str - The substring to search for
    Returns: int - Number of occurrences of the substring
    """
    return sum(1 for x in string.find(substring, 0, x != None) if x != -1)
```