```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find in the original string.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0  # Initialize a counter variable
    start = 0   # Initialize a start pointer

    # Loop through the string as long as the start pointer is within the string's bounds
    while start < len(string):
        # Find the index of the substring in the string, starting from the current start pointer
        index = string.find(substring, start)

        # If the substring is found
        if index!= -1:
            # Increment the counter
            count += 1
            # Move the start pointer to the position right after the found substring
            start = index + 1
        else:
            # If the substring is not found, break the loop
            break

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```