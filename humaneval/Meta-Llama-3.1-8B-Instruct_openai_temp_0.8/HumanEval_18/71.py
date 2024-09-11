```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.
    """
    # Handle edge cases where substring is empty
    if not substring:
        return 0

    # Initialize count to 0
    count = 0

    # Initialize current position to 0
    pos = 0

    # Loop until the substring is no longer found
    while True:
        # Find the position of the substring in the string, starting from the current position
        pos = string.find(substring, pos)

        # If the substring is not found, break the loop
        if pos == -1:
            break

        # Increment the count
        count += 1

        # Move the current position to the position after the found substring
        pos += 1

    # Return the count
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method of Python strings to find the position of the substring in the string. The `find` method returns -1 if the substring is not found. The script loops until the substring is no longer found, incrementing the count each time the substring is found.