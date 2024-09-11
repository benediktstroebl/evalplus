```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1  # Move to the next character to consider overlapping cases
        else:
            break
    return count
```

This function uses the `find` method to search for the substring in the string, starting from the current index. If the substring is found, the function increments the count and moves the index to the next character to consider overlapping cases. This process continues until the substring is no longer found in the string. The function returns the total count of occurrences.