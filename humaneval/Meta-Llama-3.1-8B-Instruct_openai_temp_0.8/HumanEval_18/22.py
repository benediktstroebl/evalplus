```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected: 0
print(how_many_times('aaa', 'a'))  # Expected: 3
print(how_many_times('aaaa', 'aa'))  # Expected: 3
```

This script defines the function `how_many_times` that takes a string and a substring as input and returns the number of times the substring can be found in the original string. The function uses a for loop to check every starting position in the string, and for each position, it checks if the substring starts at that position using the `startswith` method. The count of such positions is then returned.