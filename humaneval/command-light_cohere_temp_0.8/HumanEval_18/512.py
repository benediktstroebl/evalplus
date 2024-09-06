```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string, accounting for overlapping matches.

    Parameters:
    string (str): The input string
    substring (sub): The substring to find

    Returns:
    count: Number of occurrences of sub in str
    """
    count = 0
    for char in substring:
        count += string.find(char) == None ? 0 : 1
    return count
```