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
    if not substring:  # handle edge case where substring is empty
        return 0

    count = 0
    start = 0

    while start < len(string):
        # find the substring in the string starting from the current position
        pos = string.find(substring, start)
        
        if pos!= -1:
            # if the substring is found, increment the count and move the start position
            count += 1
            start = pos + 1
        else:
            # if the substring is not found, break the loop
            break

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```