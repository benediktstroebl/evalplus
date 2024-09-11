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
    count = 0
    for i in range(len(string)):
        # Check if the substring matches the string at the current position
        if string[i:].startswith(substring):
            count += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function called `how_many_times` that takes in a string and a substring as input. It then iterates over the string and checks if the substring matches the string at each position. If a match is found, it increments a counter. The function returns the final count of matches.