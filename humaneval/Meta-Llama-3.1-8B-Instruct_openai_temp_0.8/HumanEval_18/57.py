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

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    if not substring:  # edge case: if substring is empty, return 0
        return count
    
    string_len = len(string)
    substring_len = len(substring)

    for i in range(string_len - substring_len + 1):  # adjust the range to prevent index error
        if string[i:i + substring_len] == substring:
            count += 1

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This Python script defines a function `how_many_times` that counts the occurrences of a given substring in a string. It uses a for loop to iterate over the string, checking each substring of the same length as the target substring. If a match is found, the count is incremented. The function returns the total count. The test cases are included at the end to demonstrate the function's usage.