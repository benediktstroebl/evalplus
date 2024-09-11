```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

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
    if not substring:
        return 0  # If substring is empty, return 0
    
    count = 0
    i = 0  # Initialize the start index
    while i < len(string):
        # Use str.find() to get the index of the first occurrence of the substring
        index = string.find(substring, i)
        if index!= -1:
            count += 1
            i = index + 1  # Move the start index to the next character
        else:
            break  # If the substring is not found, break the loop
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a while loop to iterate through the string, using `str.find()` to get the index of the first occurrence of the substring at the current position `i`. If the substring is found, it increments the count and moves the start index `i` to the next character after the found substring. If the substring is not found, it breaks the loop.