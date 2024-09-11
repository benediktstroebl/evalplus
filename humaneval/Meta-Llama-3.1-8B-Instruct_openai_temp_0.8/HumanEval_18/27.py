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

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count

# Test the function
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script uses a simple for loop to iterate over the string and checks if the substring starts at each index. If it does, it increments the count. The function then returns the count.