```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring is found in the string.
    """
    if not substring:  # if the substring is empty, return 0
        return 0
    
    count = 0
    start = 0
    
    while start < len(string):
        pos = string.find(substring, start)
        
        if pos!= -1:
            count += 1
            start = pos + 1  # move the start position to the next character
        else:
            break
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring is found in the string, counting overlapping cases. It uses the `find` method to search for the substring in the string, and moves the start position to the next character after each find. The function returns 0 if the substring is empty.