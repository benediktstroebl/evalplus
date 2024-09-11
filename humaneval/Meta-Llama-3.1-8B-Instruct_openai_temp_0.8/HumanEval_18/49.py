```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the original string.
    """
    if not string or not substring:
        # If either the string or substring is empty, return 0
        return 0
    
    count = 0
    index = 0
    
    while index < len(string):
        # Find the index of the substring in the string, starting from the current index
        index = string.find(substring, index)
        
        if index == -1:
            # If the substring is not found, break the loop
            break
        
        count += 1
        # Move the index to the position right after the found substring
        index += 1
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses Python's built-in `find` method to locate the substring within the string. It maintains a counter for the number of found substrings and adjusts the search index accordingly to avoid counting overlapping cases. The script also includes initial checks to handle cases where the string or substring is empty.