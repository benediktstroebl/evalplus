```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring can be found.
    """

    # Check if the substring is empty, in which case it can be found zero times
    if not substring:
        return 0

    # Initialize a counter for the number of times the substring is found
    count = 0

    # Initialize the starting index for the search
    start = 0

    # Continue the search until the substring can no longer be found
    while True:
        # Find the index of the substring in the string, starting from the current index
        index = string.find(substring, start)

        # If the substring is not found, break the loop
        if index == -1:
            break

        # Increment the counter
        count += 1

        # Move the starting index to the position right after the found substring
        start = index + 1

    # Return the total count
    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```