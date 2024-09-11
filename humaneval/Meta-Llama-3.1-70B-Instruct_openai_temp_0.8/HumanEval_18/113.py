```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.
    """
    if not substring:  # Edge case: empty substring
        return 0
    
    count = 0
    start = 0
    while start < len(string):
        # Find the substring in the string, starting from the current position
        pos = string.find(substring, start)
        
        # If the substring is not found, break the loop
        if pos == -1:
            break
        
        # Increment the count and move the start position to the next character
        count += 1
        start = pos + 1
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```