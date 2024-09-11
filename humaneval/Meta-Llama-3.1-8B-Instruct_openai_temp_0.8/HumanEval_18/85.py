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
    # Edge case: If the substring is empty, return 0
    if not substring:
        return 0

    # Initialize a counter for the number of times the substring is found
    count = 0

    # Initialize a pointer for the current position in the string
    i = 0

    # Loop until the pointer is at the end of the string
    while i < len(string):
        # Check if the substring matches the string at the current position
        if string[i:i + len(substring)] == substring:
            # If it matches, increment the counter and move the pointer one character forward
            count += 1
            i += 1
        else:
            # If it doesn't match, move the pointer one character forward
            i += 1

    # Return the total count of matches
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring is found in the string, counting overlapping cases. The function uses a simple loop to search for the substring in the string, and it returns the total count of matches. The test cases at the end demonstrate the function's behavior.