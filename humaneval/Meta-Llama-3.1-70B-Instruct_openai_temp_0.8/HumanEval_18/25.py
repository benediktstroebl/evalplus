```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found.

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
    start = 0
    while start < len(string):  # Iterate over the string
        pos = string.find(substring, start)  # Find the substring
        if pos!= -1:  # If found
            count += 1  # Increment the count
            start = pos + 1  # Move the start position to the next character
        else:
            break  # Exit the loop if not found

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```