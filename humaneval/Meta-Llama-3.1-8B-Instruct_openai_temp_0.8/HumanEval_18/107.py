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
    i = 0
    while i < len(string):
        if string[i:].startswith(substring):
            count += 1
        i += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This Python script uses a while loop to iterate over the string, checking each position if it's possible to find the substring starting from there. If the substring matches, it increments the count. This approach counts overlapping cases and has a time complexity of O(n*m), where n is the length of the string and m is the length of the substring.