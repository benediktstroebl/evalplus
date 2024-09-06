```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find how many times a given substring can be found in the original string, 
    accounting for overlapping occurrences.
    
    Parameters: string: The input string 
    substring: The substring to search for
    
    Returns: Number of times the substring appears 
    """
    return sum(1 for i,j in enumerate(string.find(substring))
```