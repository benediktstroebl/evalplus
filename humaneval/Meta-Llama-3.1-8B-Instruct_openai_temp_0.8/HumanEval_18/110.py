```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring is found in the original string.

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # Edge case: If the substring is empty or the string is empty, return 0
    if not substring or not string:
        return 0

    # Initialize count to 0
    count = 0

    # Loop over the string with a sliding window of the length of the substring
    for i in range(len(string)):
        # Check if the substring matches the current window
        if string[i:i+len(substring)] == substring:
            # If it matches, increment the count
            count += 1

    # Return the total count
    return count
```

You can use this script as a self-contained module to find the number of times a substring appears in a string, counting overlapping cases.