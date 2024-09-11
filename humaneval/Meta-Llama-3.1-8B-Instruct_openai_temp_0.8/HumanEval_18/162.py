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
    if not substring:  # Check if the substring is empty
        return 0

    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)  # Find the next occurrence of the substring
        if index!= -1:  # If the substring was found
            count += 1
            index += 1  # Move the index to the character after the found substring
        else:
            break

    return count

# Test cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This script uses the `str.find()` method to find the next occurrence of the substring in the string. It increments a counter each time a match is found and moves the index to the character after the found substring. This process continues until no more matches can be found. If the substring is empty, the function immediately returns 0.