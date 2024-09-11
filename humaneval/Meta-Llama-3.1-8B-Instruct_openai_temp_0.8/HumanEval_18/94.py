```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0
    for i in range(len(string)):
        # Check if the substring matches the string starting from index i
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

# Example usage:
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script works by iterating over the original string and checking if the substring matches the string starting from each index `i`. If a match is found, it increments the count. This way, overlapping cases are counted correctly.