```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the original string.

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:
        # If the substring is empty, return 0 because an empty substring cannot be found
        return 0
    
    count = 0
    index = 0
    # Use the end index to start searching from the end of the last match
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            # If the substring is not found, break out of the loop
            break
        count += 1
        # Move the end index to the end of the current match
        index += 1
    
    return count
```

This script uses the `find` method of the string class to find the index of the substring in the original string. If the substring is found, it increments the count and moves the end index to the end of the current match. It continues this process until the substring is no longer found. The function returns the count of times the substring is found.