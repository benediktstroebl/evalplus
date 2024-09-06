```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string, 
    while avoiding overlapping occurrences.

    Args: 
        string: The input string 
        substring: The substring to search for

    Returns: 
        int: Number of times the substring appears in the string
    """
    return sum(1 for _ in string.find(substring, string))
```
The function uses the findall function to find all the occurrences of the substring in the string, and then sums the number of calls to get the total count.