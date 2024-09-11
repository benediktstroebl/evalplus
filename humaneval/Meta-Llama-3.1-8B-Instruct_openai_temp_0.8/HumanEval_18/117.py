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
    count = 0
    for i in range(len(string)):
        # Check if the substring is found at the current position
        if string[i:].startswith(substring):
            count += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script works by iterating over each position in the original string, and for each position, it checks if the substring can be found starting at that position. If it can, it increments the count. The `str.startswith()` method is used to check if the substring can be found at the current position. This method returns `True` if the string starts with the given substring, and `False` otherwise. The `str[i:]` syntax is used to get the substring of the original string starting at position `i`.