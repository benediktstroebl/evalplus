```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring appears in the string.
    """
    if not substring:  # If the substring is empty, return 0
        return 0

    count = 0  # Initialize the count
    start = 0  # Initialize the start index

    while start < len(string):  # Loop through the string
        pos = string.find(substring, start)  # Find the substring
        if pos!= -1:  # If the substring is found
            count += 1  # Increment the count
            start = pos + 1  # Move the start index to the next position
        else:
            break  # If the substring is not found, break the loop

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```