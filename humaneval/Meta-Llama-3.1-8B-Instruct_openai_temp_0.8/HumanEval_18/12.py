```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    
    Args:
    string (str): The original string.
    substring (str): The substring to be found.
    
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
    start = 0
    
    while start < len(string):
        pos = string.find(substring, start)
        
        if pos!= -1:
            count += 1
            start = pos + 1
        else:
            break
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method of the string class to search for the substring in the original string. If the substring is found, it increments the count and moves the start position to the character after the found substring. This allows for overlapping cases. The process continues until the substring is not found anymore. The function returns the total count of times the substring was found.