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
    count = 0  # Initialize a counter variable to store the number of occurrences
    start = 0  # Initialize a start index to begin searching from

    # Continue searching until the start index is beyond the length of the string
    while start < len(string):
        # Use the str.find() method to find the index of the substring
        # starting from the current start index
        pos = string.find(substring, start)

        # If the substring is not found, str.find() returns -1, so break the loop
        if pos!= -1:
            # If the substring is found, increment the counter and update the start index
            # to continue searching from the next character
            count += 1
            start = pos + 1
        else:
            break

    return count


# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```