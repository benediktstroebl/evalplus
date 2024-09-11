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
        # Check if the substring is present at the current position
        if string[i:i+len(substring)] == substring:
            count += 1
        i += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring can be found in the string. The function uses a while loop to iterate over the string, checking each position to see if the substring is present. If it is, it increments the count. If not, it moves on to the next position. This process continues until the end of the string is reached, at which point the count is returned.