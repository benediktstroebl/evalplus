```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    considering overlapping matches.

    Parameters:
    string (str): The original string 
    substring (substring): The substring to search 
    Returns: number of times substring can be found in string
    """
    return sum(1 for x in string.contains(substring))
```
This Python function, `how_many_times`, takes two parameters: a string (`string`) and a substring (`substring`).  It returns an integer representing the number of times the `substring` can be found in the `string`, considering case-insensitive matching and counting overlapping occurrences.  The unique way this with a built-in iterable `contains` method that generates an iterator over the occurrences of the `substring` in the `string`.  This method is more efficient than using a `set` data structure.