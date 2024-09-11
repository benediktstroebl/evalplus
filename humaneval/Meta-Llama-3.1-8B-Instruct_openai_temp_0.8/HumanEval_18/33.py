```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

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
    string_index = 0
    while string_index < len(string):
        # Find the index of the substring in the string
        index = string.find(substring, string_index)
        
        # If the substring is not found, break the loop
        if index == -1:
            break
        
        # Increment the count and move the string index to the right
        count += 1
        string_index = index + 1
    
    return count

# Test the function
print(how_many_times('', 'a'))
print(how_many_times('aaa', 'a'))
print(how_many_times('aaaa', 'aa'))
```

This script uses the built-in `find` method of Python strings to find the index of the substring in the string. It then increments a count and moves the string index to the right of the found substring, effectively sliding a window over the string to count overlapping occurrences. The loop continues until the substring is no longer found in the string.