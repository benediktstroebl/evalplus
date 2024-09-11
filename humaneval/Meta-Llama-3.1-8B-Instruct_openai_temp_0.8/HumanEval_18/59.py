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
    if not substring:  # If substring is empty, return 0
        return 0
    
    count = 0
    pos = 0
    while True:
        pos = string.find(substring, pos)  # Find the next occurrence of the substring
        if pos!= -1:  # If the substring is found
            count += 1  # Increment the count
            pos += 1  # Move the position to the next character
        else:
            break  # If the substring is not found, break the loop
    
    return count  # Return the count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method of the string class to find the next occurrence of the substring in the string. It then increments the count and moves the position to the next character. The loop continues until the substring is not found in the string. The function returns the count of the occurrences of the substring in the string.