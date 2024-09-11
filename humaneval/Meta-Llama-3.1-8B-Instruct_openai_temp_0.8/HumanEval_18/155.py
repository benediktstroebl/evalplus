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
    """
    # If the substring is empty or the string is empty, return 0
    if not substring or not string:
        return 0
    
    # Initialize a counter for the number of occurrences
    count = 0
    
    # Initialize a pointer for the current position in the string
    pos = 0
    
    # Search for the substring in the string
    while pos < len(string):
        # Find the position of the substring in the string starting from the current position
        pos = string.find(substring, pos)
        
        # If the substring is not found, break the loop
        if pos == -1:
            break
        
        # Increment the counter
        count += 1
        
        # Move the position to the end of the found substring
        pos += 1
    
    # Return the count of occurrences
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script implements the `how_many_times` function to count the number of occurrences of a given substring in a string, considering overlapping cases. It uses the `find` method to search for the substring in the string, starting from the current position, and increments a counter each time it finds the substring. The loop continues until the end of the string is reached or the substring is not found. The function returns the count of occurrences.