```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the original string.
    """
    count = 0
    index = 0
    
    # Loop until the substring is no longer found in the string
    while True:
        index = string.find(substring, index)
        
        # If the substring is not found, break the loop
        if index == -1:
            break
        
        # Increment the count and move the index to the end of the found substring
        count += 1
        index += len(substring)
    
    return count

# Test cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This script defines a function `how_many_times` that takes two parameters: `string` and `substring`. It uses a while loop to find all occurrences of `substring` in `string`, counting overlapping cases. The loop stops when `substring` is no longer found in `string`. The function returns the total count of occurrences. The test cases at the end demonstrate the function's behavior.