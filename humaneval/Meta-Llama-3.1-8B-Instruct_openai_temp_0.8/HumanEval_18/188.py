```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
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
    i = 0
    while i < len(string):
        # Check if the substring matches at the current position
        if string[i:i+len(substring)] == substring:
            count += 1
            # Move the current position forward to find the next match
            i += 1
        i += 1
    return count
```

This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring appears in the string, counting overlapping cases. It uses a while loop to iterate through the string and checks each position to see if it matches the beginning of the substring. If it does, it increments the count and moves the current position forward by one. The function then returns the count.