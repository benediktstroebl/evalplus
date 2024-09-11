```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    index = 0

    while index < len(string):
        index = string.find(substring, index)
        
        if index == -1:  # substring not found
            break
        
        count += 1
        index += 1  # move index to the next character after the found substring

    return count
```

This script uses the `find` method of Python's string class, which returns the index of the first occurrence of the substring in the string. If the substring is not found, it returns `-1`, and we use this to break the loop when the substring is not found anymore.