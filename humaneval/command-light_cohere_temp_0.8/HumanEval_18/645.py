```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    This function returns the number of occurrences of a given substring within the original string, 
    considering cases with overlapping substrings.

    Args: 
        string: The input string 
        substring: The substring to search for 
    Returns: 
        int: Number of occurrences of the substring
    """
    return sum(1 for x in string.find(substring, 0, len(substring))
```