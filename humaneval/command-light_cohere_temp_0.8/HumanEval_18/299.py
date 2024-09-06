```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string, 
    considering overlapping matches.

    Parameters:
    string (str): The original string
    substring (sub): The substring to search for

    Returns:
    int: Number of occurrences of sub in string
    """
    return sum(1 for i, j in enumerate(string.find(substring))
```
Do you need any further assistance with this problem or code?