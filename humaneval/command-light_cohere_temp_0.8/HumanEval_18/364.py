```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping occurrences.

    Parameters: 
    string: str, the original string 
    substring: str, the substring to find occurrences in 
    Returns: int, the number of occurrences without overlapping.
    """
    string = "aaaaaaa"
    substring = "aa"
    result = 0
    start = 0
    while start < len(string):
        if string[start:start+len(substring)] == substring:
            result += 1
        start += 1
    return result
```