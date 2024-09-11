```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the string.
    """
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    start_idx = 0
    while start_idx < len(string):
        idx = string.find(substring, start_idx)
        if idx!= -1:
            count += 1
            start_idx = idx + 1  # move start index to the next character
        else:
            break

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```