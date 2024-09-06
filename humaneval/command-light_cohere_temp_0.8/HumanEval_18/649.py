```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Purpose: Find how many times a given substring can be found in the original string, 
    counting overlapping occurrences.

    Parameters: 
    string: str - Original text string 
    substring: str - Substring to search for

    Returns: int - Count of occurrences of the substring
    """
    return sum(1 for i, j in enumerate(string.join(substring), string[j:i+1]) for i, j in enumerate(substring))
```