```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    # Initialize the count to 0
    count = 0
    
    # If the substring is empty, return 0
    if not substring:
        return count
    
    # Initialize the start index to 0
    start = 0
    
    # Loop until the start index is less than the length of the string
    while start < len(string):
        
        # Find the index of the substring in the string, starting at the current start index
        index = string.find(substring, start)
        
        # If the substring is not found, break the loop
        if index == -1:
            break
        
        # Increment the count
        count += 1
        
        # Move the start index to the index after the found substring
        start = index + 1
    
    # Return the count
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the built-in `find` method of Python strings to find the index of the substring in the original string. It then increments the count and moves the start index to the index after the found substring, effectively allowing for overlapping matches. If the substring is not found, it breaks the loop and returns the count.