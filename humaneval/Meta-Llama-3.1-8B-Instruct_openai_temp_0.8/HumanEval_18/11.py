```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring appears in the string.

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
        if string[i:i+len(substring)] == substring:
            count += 1
            i += 1
        i += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes two strings, `string` and `substring`, and returns the number of times `substring` appears in `string`. It uses a simple loop to iterate through the characters in `string`, checking if the current substring matches `substring`. If it does, it increments the count and moves the index forward by one. If it doesn't, it simply moves the index forward by one. The function returns the count at the end.