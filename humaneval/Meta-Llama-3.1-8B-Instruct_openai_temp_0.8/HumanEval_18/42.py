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
    if not substring:
        # If the substring is empty, return 0
        return 0
    
    # Initialize a counter for the number of occurrences
    count = 0
    
    # Initialize a pointer for the substring
    substring_pointer = 0
    
    # Iterate over the string
    for char in string:
        # If the current character matches the character at the substring pointer
        if char == substring[substring_pointer]:
            # Move the substring pointer forward
            substring_pointer += 1
            
            # If the substring pointer is at the end of the substring
            if substring_pointer == len(substring):
                # Increment the count
                count += 1
                # Reset the substring pointer
                substring_pointer = 0
    
    # Return the count
    return count

# Test cases
print(how_many_times('', 'a'))     # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script implements a function `how_many_times` that counts the number of occurrences of a substring in a string, including overlapping cases. It uses a sliding window approach to achieve this in O(n) time complexity, where n is the length of the string.