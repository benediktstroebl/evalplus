```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the original string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    start = 0

    # Loop through the string, shifting the window by the length of the substring
    while start < len(string):
        # Check if the substring matches the current window
        if string[start:].startswith(substring):
            # If it does, increment the count and move the window forward
            count += 1
            start += 1
        else:
            # If it doesn't, move the window forward
            start += 1

    return count
```

You can test this function using the provided examples or with your own inputs.