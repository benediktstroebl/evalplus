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
    if not substring:  # edge case: if the substring is empty
        return 0
    
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:  # found a match
            count += 1
            start = pos + 1  # move the start position to the right of the match
        else:
            break  # no more matches

    return count

# Test cases
print(how_many_times('', 'a'))   # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that counts the number of times a given substring appears in a string, including overlapping cases. It uses a while loop and the `find` method of the string to find the first occurrence of the substring, and then increments the count and moves the start position to the right of the match. It continues this process until no more matches are found.