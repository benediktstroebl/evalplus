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
    string_len = len(string)
    substring_len = len(substring)
    
    # Handle edge case where substring is empty
    if substring_len == 0:
        return string_len + 1
    
    # Handle edge case where string is empty or substring is longer than the string
    if string_len == 0 or substring_len > string_len:
        return 0
    
    # Use a sliding window approach to find overlapping matches
    for i in range(string_len - substring_len + 1):
        if string[i:i + substring_len] == substring:
            count += 1
    
    return count

# Example use cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script uses a sliding window approach to find all occurrences of the substring in the string, including overlapping cases. It iterates over the string, checking each substring of the same length as the target substring. If a match is found, it increments the count. Finally, it returns the count, which represents the number of times the substring can be found in the string.