```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    count = 0
    start = 0  # Start index for searching

    # Continue searching until the start index is less than the length of the string
    while start < len(string):
        # Find the index of the substring in the string starting from the current start index
        pos = string.find(substring, start)

        # If the substring is found
        if pos!= -1:
            # Increment the count
            count += 1
            # Move the start index to the position right after the found substring
            start = pos + 1
        else:
            # If the substring is not found, break the loop
            break

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a while loop to continuously search for the substring in the string, starting from the last found position. The `find` method returns the index of the first occurrence of the substring, or -1 if it is not found. The `start` variable keeps track of the current search position. If the substring is found, the `count` is incremented and the search position is moved right after the found substring. If the substring is not found, the loop breaks and the function returns the count.