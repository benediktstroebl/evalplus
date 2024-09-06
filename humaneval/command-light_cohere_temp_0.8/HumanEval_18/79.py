Here is a self-contained Python function that solves the problem of counting the number of occurrences of a given substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of times a given substring can be found in the original string, 
    taking overlapping occurrences into account.

    Parameters: 
    string: str, The input string 
    substring: str, The substring to search for 
    Returns: int, Number of times the substring appears in the string
    """
    return len({(string.count(substring) for substring in set(substring)})
``` 
This function uses a Python set to efficiently count the occurrences of the substring in the input string, accounting for overlapping occurrences. The function also returns the number of times the substring appears in the original string.