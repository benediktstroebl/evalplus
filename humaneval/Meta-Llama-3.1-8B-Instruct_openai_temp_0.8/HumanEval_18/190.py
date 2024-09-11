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

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:
        return 0  # edge case: empty substring cannot be found

    count = 0
    index = 0

    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        count += 1
        index += 1  # move to the position right after the matched substring

    return count
```

This function uses the built-in `find` method of Python strings, which returns the index of the first occurrence of the substring, or -1 if it's not found. It starts searching from the current index for each iteration, effectively counting overlapping matches. If the substring is not found, the `find` method returns -1 and the loop breaks.