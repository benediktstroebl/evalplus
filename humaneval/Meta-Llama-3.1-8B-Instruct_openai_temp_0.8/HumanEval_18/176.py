```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0
    i = 0
    while i < len(string):
        # Find the substring in the string starting from index i
        index = string.find(substring, i)
        if index!= -1:
            # If found, increment the count and move the index to the end of the found substring
            count += 1
            i = index + len(substring)
        else:
            # If not found, break the loop
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script defines a function `how_many_times` that searches for a given substring in an original string and returns the number of times it can be found, including overlapping cases. The function uses a while loop to iterate through the string and the `find` method to search for the substring. If the substring is found, the count is incremented and the index is moved to the end of the found substring. If the substring is not found, the loop breaks.