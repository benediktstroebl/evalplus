```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Calculates and returns the number of times the substring can be found in the string without overlapping.

    Args:
        string: str, The original string 
        where substring could appear
        substring: str, The substring to find

    Returns: int, The number of occurrences of substring in string
    """
    return len(string.find(substring, string))
```