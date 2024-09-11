```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be searched.

    Returns:
    int: The number of times the substring is found in the string.
    """
    if not substring:  # if substring is empty, return 0
        return 0

    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script works by iterating over the string with a sliding window of the same length as the substring. If the substring matches the current window, it increments the count. This way, it correctly counts overlapping occurrences of the substring.