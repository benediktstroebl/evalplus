```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of occurrences of the substring in the string.

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # Handle edge case where substring is empty
    if not substring:
        return 0

    # Initialize a counter to store the number of occurrences
    count = 0
    
    # Initialize a pointer to the current position in the string
    i = 0
    
    # Iterate over the string
    while i < len(string):
        
        # Check if the substring matches the string at the current position
        if string[i:i + len(substring)] == substring:
            
            # If a match is found, increment the counter
            count += 1
        
        # Move the pointer to the next position
        i += 1
    
    # Return the total count of occurrences
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This Python script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring appears in the string, counting overlapping cases. The function iterates over the string, checking for matches with the substring at each position, and increments a counter for each match found. The final count is then returned.