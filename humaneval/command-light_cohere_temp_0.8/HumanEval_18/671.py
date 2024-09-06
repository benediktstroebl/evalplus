```python
def how_many_times(string: str, substring: str) -> int:
    """
    Returns number of occurrences of substring in string, counting overlapping occurrences as valid.
    Parameters: 
    string: str - The input string 
    substring: str - The substring to search for in the input string
    Returns: 
    int - Number of occurrences of the substring in the input string
    """
    return len(string.find(substring))
```