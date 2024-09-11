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
    if not substring:  # If the substring is empty, return 0
        return 0
    
    count = 0
    index = 0
    while index < len(string):  # Continue searching until the end of the string is reached
        index = string.find(substring, index)  # Find the substring starting from the current index
        if index!= -1:  # If the substring is found
            count += 1
            index += 1  # Move the index to the character after the found substring
        else:
            break  # If the substring is not found, break the loop
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string. The function uses the `find` method of the `str` class to find the substring, and keeps track of the number of times it is found. If the substring is empty, the function returns 0 immediately. The function also handles overlapping cases, where the same part of the string can be found multiple times. The test cases at the end demonstrate the function's behavior.