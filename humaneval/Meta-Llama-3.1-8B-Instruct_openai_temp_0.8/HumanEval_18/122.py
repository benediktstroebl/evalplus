```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    count = 0
    index = 0
    # Continue searching for the substring until we've searched the entire string
    while index < len(string):
        # Find the index of the substring in the string, starting from the current index
        index = string.find(substring, index)
        # If the substring is found, increment the count and move the index to the end of the found substring
        if index!= -1:
            count += 1
            index += 1
        # If the substring is not found, break the loop
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script uses a while loop to iteratively search for the substring in the original string, starting from the current index. If the substring is found, the count is incremented and the index is moved to the end of the found substring. If the substring is not found, the loop breaks and the function returns the count.