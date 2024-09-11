### Solution: Counting Overlapping Substring Occurrences
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the original string.
    """
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
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This script defines a function `how_many_times` that uses a while loop to repeatedly search for the substring in the string, starting from the previous found position. The `find` method returns the position of the first occurrence of the substring, or -1 if it's not found. If the substring is found, the function increments the count and updates the start position to the position after the found substring. This process continues until the substring is no longer found in the string.