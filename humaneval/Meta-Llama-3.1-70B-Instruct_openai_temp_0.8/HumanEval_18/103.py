```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring is found in the string.
    """
    # Initialize count to 0
    count = 0
    
    # If the substring is empty, return 0
    if not substring:
        return 0
    
    # Iterate over the string with a sliding window of the substring's length
    for i in range(len(string) - len(substring) + 1):
        # If the substring matches the current window, increment the count
        if string[i:i+len(substring)] == substring:
            count += 1
    
    # Return the total count
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring appears in the string, counting overlapping cases. The function uses a sliding window approach to iterate over the string and check for matches with the substring. If a match is found, the count is incremented. The function returns the total count after iterating over the entire string. The script also includes test cases to verify the function's behavior.