```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    Count overlapping cases.
    
    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.
    
    Returns:
    int: The number of times the substring can be found in the string.
    
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    index = 0
    
    # Continue searching for the substring until it is no longer found
    while True:
        # Find the index of the substring in the string, starting from the current index
        index = string.find(substring, index)
        
        # If the substring is not found, break the loop
        if index == -1:
            break
        
        # Increment the count and move the index to the position after the found substring
        count += 1
        index += 1
    
    return count

print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the built-in `find` method of Python strings, which returns the index of the first occurrence of the substring, or -1 if the substring is not found. The loop continues until the substring is no longer found, at which point the count is returned.