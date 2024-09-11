```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found.
    """
    if not substring:  # If the substring is empty, return 0.
        return 0
    
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # Move the start position to the next character.
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that uses the `find` method to locate the substring in the string. The `find` method returns the position of the first occurrence of the substring, or -1 if the substring is not found. The `while` loop continues to search for the substring until it is no longer found. The `start` position is updated to the character after the found substring to allow for overlapping matches.