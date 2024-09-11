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
    """
    if not substring:  # if substring is empty, return 0
        return 0

    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # move start to the next character after the found substring
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method of the string class to search for the substring. The `find` method returns the index of the first occurrence of the substring, or -1 if the substring is not found. The `start` variable is used to keep track of the current position in the string, and is updated to the position after the found substring after each iteration. The count is incremented each time a substring is found.