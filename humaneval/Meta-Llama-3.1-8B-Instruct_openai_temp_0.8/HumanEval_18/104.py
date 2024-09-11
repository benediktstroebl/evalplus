```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring is found.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            start = pos + 1
            count += 1
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a while loop to iterate over the string, using the `find` method with a start position to find the next occurrence of the substring. If it's found, the start position is updated to the position after the found substring, and the count is incremented. If it's not found (i.e., the `find` method returns -1), the loop breaks. The loop continues until the entire string has been searched.