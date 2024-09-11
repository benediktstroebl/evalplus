```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

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
    string_length = len(string)
    substring_length = len(substring)
    if not substring:
        return string_length
    for i in range(string_length):
        if string[i:i + substring_length] == substring:
            count += 1
    return count
```

In this script, we define the function `how_many_times` which takes two parameters: the original string and the substring. It initializes a counter to 0 and uses a for loop to check each substring of the same length as the substring we are looking for in the original string. If it finds a match, it increments the counter. Finally, it returns the counter.

Note: This function considers overlapping cases by comparing substrings of the same length, so it counts 'a' in 'aba' as 3, not 2. If you want to count non-overlapping cases, you can use the `count` method of Python strings, but you would need to adjust the logic of the function accordingly.