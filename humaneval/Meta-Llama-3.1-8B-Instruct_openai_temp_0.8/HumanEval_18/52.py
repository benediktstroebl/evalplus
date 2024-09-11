```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring appears in the string.
    """
    count = 0
    for i in range(len(string)):
        # Check if the substring matches the string starting at index i
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines the `how_many_times` function, which iterates over the original string and checks for each position if the substring matches the corresponding part of the string. If a match is found, it increments the count. The function returns the total count. The test cases at the end demonstrate the function's behavior.