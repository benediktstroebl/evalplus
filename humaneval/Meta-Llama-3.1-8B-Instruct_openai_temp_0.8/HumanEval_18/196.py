```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of occurrences of the substring in the string.
    """
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    index = 0  # keep track of the current position in the string

    while index < len(string):
        index = string.find(substring, index)  # find the next occurrence of the substring
        if index == -1:  # if not found, break the loop
            break
        count += 1
        index += 1  # move to the position after the found substring

    return count

# Example usage:
print(how_many_times('', 'a'))     # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This code uses a while loop to keep finding the next occurrence of the substring in the string, incrementing a counter for each found occurrence. It also handles the edge case where the substring is empty, returning 0 in that case.