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
    if not substring:  # Handle edge case where substring is empty
        return 0

    count = 0
    start = 0
    while start < len(string):
        # Find the index of the substring in the string, starting from'start'
        index = string.find(substring, start)
        if index!= -1:
            # If the substring is found, increment the count and move'start' to the next character
            count += 1
            start = index + 1
        else:
            # If the substring is not found, break out of the loop
            break

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```