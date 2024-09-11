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

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    if not substring:  # Edge case: if the substring is empty
        return 0
    
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:  # If the substring is found
            count += 1
            index += 1  # Move the search index forward by 1 to avoid overlapping matches
        else:
            break
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string, considering overlapping cases. It uses a while loop to repeatedly search for the substring in the string, starting from the current index, and increments the count each time it finds a match. The search index is moved forward by 1 after each match to avoid overlapping matches. If the substring is not found, the loop breaks, and the function returns the count.