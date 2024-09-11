```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.
    """
    # Handle edge case where substring is empty
    if not substring:
        return 0

    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1
        else:
            break

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```
This script defines the `how_many_times` function as specified, which counts the number of times a given substring appears in a string, including overlapping cases. The function uses the `find` method to locate the substring in the string, starting from the current position `start`. If the substring is found, the count is incremented and the start position is moved to the position after the found substring. This process continues until the end of the string is reached.