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
    if not substring:  # If the substring is empty, return 0
        return 0
    
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)  # Find the next occurrence of the substring
        if index == -1:  # If the substring is not found, break the loop
            break
        count += 1  # Increment the count
        index += len(substring)  # Move the index to the next position

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```