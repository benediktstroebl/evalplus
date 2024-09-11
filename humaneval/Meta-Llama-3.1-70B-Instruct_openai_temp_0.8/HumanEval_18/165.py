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
    if not substring:  # If the substring is empty, it's not found
        return 0

    count = 0  # Initialize the count of occurrences
    start = 0  # Start searching from the beginning of the string

    while start < len(string):  # Continue searching until we reach the end of the string
        pos = string.find(substring, start)  # Find the substring in the string
        if pos!= -1:  # If the substring is found
            count += 1  # Increment the count
            start = pos + 1  # Continue searching from the position after the found substring
        else:
            break  # If the substring is not found, stop searching

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```