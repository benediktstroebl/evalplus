```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string, 
    considering overlapping matches.
    Parameters: 
    string (str): Input string 
    substring (str): Substring to search for 
    Returns: Number of occurrences of substring in string
    """
    return sum(1 for x in string.find(substring, 0, len(substring) > 0))
```