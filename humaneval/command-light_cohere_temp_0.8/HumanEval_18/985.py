```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping.

    Parameters:
    string: str, the original string 
    substring: str, the substring to find

    Returns: 
    int: the number of positions where substring can be found in string
    """
    # Remove all occurrences of substring from string by using set()
    set1 = set(string)
    set2 = set(substring)
    return len(set1.inter(set2))
```