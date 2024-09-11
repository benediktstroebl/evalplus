```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    start = 0
    while True:
        start = string.find(substring, start)  # find the next occurrence
        if start == -1:  # not found
            break
        count += 1
        start += 1  # move the start point to the right of the found substring
    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines the `how_many_times` function, which counts the number of times a given substring appears in an original string, including overlapping cases. The function uses a while loop to find each occurrence of the substring and increments the count accordingly. It handles the edge case where the substring is empty by returning 0 immediately. The test cases at the end demonstrate the function's behavior with various inputs.