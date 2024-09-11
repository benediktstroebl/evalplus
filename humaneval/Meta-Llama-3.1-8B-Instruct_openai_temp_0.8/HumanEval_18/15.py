```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    
    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.
    
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
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string, counting overlapping cases. The function uses a while loop to repeatedly search for the substring, starting from the current position in the string. If the substring is found, the loop increments the count and starts searching from the position after the found substring. The loop continues until the substring is no longer found.