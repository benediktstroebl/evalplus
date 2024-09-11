```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    count = 0
    string_len, substring_len = len(string), len(substring)
    for i in range(string_len - substring_len + 1):
        if string[i:i + substring_len] == substring:
            count += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a simple loop to go through the original string, checking each substring of the same length as the given substring. If a match is found, it increments the count. The loop stops when there are not enough characters left in the string to form a substring of the given length.