```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    including cases of overlapping substring.

    Parameters: 
    string (str): The input string 
    substring (sub): The substring to search

    Returns: 
    int: Number of occurrences of the substring in the string
    """
    return len(string.find(substring))
```