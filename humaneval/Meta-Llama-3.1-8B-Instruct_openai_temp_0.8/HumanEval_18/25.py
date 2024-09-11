```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to find in the original string.

    Returns:
    int: The number of times the substring can be found in the original string.

    Example:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    if not substring:  # edge case: empty substring
        return 0
    string_len = len(string)
    substring_len = len(substring)
    for i in range(string_len):
        if string[i:i + substring_len] == substring:
            count += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines the `how_many_times` function, which takes a string and a substring as input and returns the number of times the substring can be found in the original string. It uses a for loop to iterate over the original string and checks each substring of the same length as the given substring. If a match is found, it increments the count. Finally, it returns the count. The script also includes test cases to verify the function's correctness.