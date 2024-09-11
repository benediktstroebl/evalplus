```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    if not substring:
        return 0
    
    count = 0
    index = 0
    
    while index < len(string):
        index = string.find(substring, index)
        
        if index!= -1:
            count += 1
            index += 1  # Move the index to the character after the found substring
        else:
            break
    
    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method of Python's `str` class to find the index of the first character of the substring in the string, starting from the current index. If the substring is found, it increments the count and moves the index to the character after the found substring, effectively counting overlapping cases. This process repeats until the substring cannot be found anymore.