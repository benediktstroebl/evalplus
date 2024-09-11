```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0
    start = 0

    # Continue searching until the substring is no longer found
    while True:
        # Find the index of the substring in the string, starting from the current start position
        index = string.find(substring, start)

        # If the substring is not found, break the loop
        if index == -1:
            break

        # Increment the count and update the start position
        count += 1
        start = index + 1

    return count


# Test cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

In this code, we use a while loop to repeatedly search for the substring in the string, starting from the current position. The `find` method returns the index of the substring if found, and -1 otherwise. We increment the count whenever the substring is found, and update the start position to be one character after the found substring. This ensures that we count overlapping cases. The loop continues until the substring is no longer found, at which point we return the count.