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
    if not substring:  # If substring is empty, return 0 immediately
        return 0

    length = len(substring)
    for i in range(len(string)):
        if string[i:i + length] == substring:  # Check if the substring matches
            count += 1  # If it does, increment the count
    return count

# Test cases
print(how_many_times('', 'a'))  # Should print 0
print(how_many_times('aaa', 'a'))  # Should print 3
print(how_many_times('aaaa', 'aa'))  # Should print 3
```

This Python script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring can be found in the string, counting overlapping cases. The test cases at the end demonstrate the function's correctness.