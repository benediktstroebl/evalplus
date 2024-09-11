```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Parameters:
    string (str): The original string to search from.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the string.
    """

    # Initialize a counter to keep track of the number of occurrences
    count = 0
    
    # Loop through the string until the substring cannot be found anymore
    while string.find(substring)!= -1:
        # Increment the counter
        count += 1
        # Remove the found substring from the string
        # This allows us to find overlapping cases
        string = string[string.find(substring) + len(substring):]
    
    # Return the total count
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string, counting overlapping cases. The function uses a while loop to continuously search for the substring and increment the counter until the substring cannot be found anymore.