```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find in the original string.

    Returns:
        int: The number of times the substring can be found in the original string.

    Example:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    i = 0
    while i < len(string):
        if string[i:i+len(substring)] == substring:
            count += 1
        i += 1
    return count
```

This script uses a simple while loop to iterate over the original string, checking each substring of the same length as the given substring to see if it matches. If it does, the count is incremented. This process repeats until the end of the original string is reached, at which point the total count is returned.