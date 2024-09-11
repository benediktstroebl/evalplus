```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    
    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

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
    if not substring:  # If the substring is empty, return 0
        return 0
    
    count = 0
    index = 0
    while index < len(string):  # Loop through the string
        index = string.find(substring, index)  # Find the next occurrence of the substring
        if index!= -1:  # If found
            count += 1  # Increment the count
            index += 1  # Move the index to the next character
        else:
            break
    
    return count

# Test cases
print(how_many_times('', 'a'))
print(how_many_times('aaa', 'a'))
print(how_many_times('aaaa', 'aa'))
```