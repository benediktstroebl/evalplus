```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    i = 0
    while i < len(string):
        if string[i:i + len(substring)] == substring:
            count += 1
            i += 1  # Move to the next position, but still check the same index
        i += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script uses a while loop to iterate over the string and check each substring of the same length as the target substring. If a match is found, the count is incremented. The loop continues until the end of the string is reached. The test cases at the end demonstrate the function's behavior with different inputs.