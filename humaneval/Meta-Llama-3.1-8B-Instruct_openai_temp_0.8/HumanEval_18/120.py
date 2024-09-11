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
    # If the substring is empty, it can be considered to appear an infinite number of times in any string
    if not substring:
        return float('inf')
    
    # If the string is empty, the substring cannot appear in it
    if not string:
        return 0
    
    # Initialize a counter for the occurrences of the substring
    count = 0
    
    # Initialize a pointer to the current position in the string
    i = 0
    
    # Loop until the current position is beyond the string
    while i < len(string):
        # Find the position of the substring in the string, starting from the current position
        j = string.find(substring, i)
        
        # If the substring is not found, break the loop
        if j == -1:
            break
        
        # Increment the counter
        count += 1
        
        # Move the current position to the position right after the found substring
        i = j + 1
    
    # Return the total count
    return count
```

Example use cases:

```python
# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```