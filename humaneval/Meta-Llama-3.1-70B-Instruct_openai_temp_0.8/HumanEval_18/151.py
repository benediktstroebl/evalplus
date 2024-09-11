```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be found.

    Returns:
    int: The number of times the substring is found in the string.

    """
    # Handle the edge case where the substring is empty
    if not substring:
        return 0
    
    # Initialize a counter to store the number of occurrences
    count = 0
    
    # Initialize a pointer to the current position in the string
    i = 0
    
    # Loop through the string until we've checked all possible positions
    while i < len(string):
        # Check if the substring matches the string at the current position
        if string[i:i+len(substring)] == substring:
            # If it matches, increment the counter
            count += 1
        # Move the pointer to the next position
        i += 1
    
    # Return the total count of occurrences
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```