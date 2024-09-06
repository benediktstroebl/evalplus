```python
def how_many_times(string: str, substring: str) -> int:
    """
    Purpose: Find how many times a given substring can be found in the original string, without overlapping.
    Args: 
    string: The input string 
    substring: The substring to search
    Returns: count of occurrences
    """
    return sum(1 for x in string.find(substring, 0, x != None))
```