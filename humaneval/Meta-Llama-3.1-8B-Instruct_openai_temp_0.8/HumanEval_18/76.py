```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring appears in the string.
    """
    # Base case: If the substring is empty, return 0
    if not substring:
        return 0
    
    # Initialize count to 0
    count = 0
    
    # Initialize index to 0 (start of the string)
    index = 0
    
    # Loop until the substring is not found in the string
    while True:
        # Find the index of the substring in the string starting from the current index
        index = string.find(substring, index)
        
        # If the substring is not found, break the loop
        if index == -1:
            break
        
        # Increment the count
        count += 1
        
        # Move the index to the position right after the found substring
        index += 1
    
    # Return the count
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring appears in the string, counting overlapping cases. It uses a while loop to find the substring in the string, incrementing the count each time it finds the substring. The loop continues until the substring is not found in the string. The function then returns the count. The script also includes test cases to verify the function's correctness.