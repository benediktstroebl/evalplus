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

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1  # Move to the next character to find overlapping matches
        else:
            break
    return count

# Test the function
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a loop to find all occurrences of the substring in the string, and it keeps track of the current position in the string with the `index` variable. When it finds a match, it increments the count and moves to the next character to find overlapping matches. This process continues until it reaches the end of the string or cannot find a match. The function returns the total count of matches.