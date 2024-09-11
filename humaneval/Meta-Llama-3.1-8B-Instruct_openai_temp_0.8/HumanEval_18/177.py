```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Consider overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    if not substring:  # if substring is empty
        return 0
    count = 0
    start = 0
    while start < len(string):
        idx = string.find(substring, start)
        if idx!= -1:
            count += 1
            start = idx + 1
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This Python script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the original string. It considers overlapping cases.

The function uses a while loop to find all occurrences of the substring in the string. It keeps track of the starting position of the next search with the `start` variable. If the substring is found, the function increments the count and moves the start position to the position right after the found substring. If the substring is not found, it breaks out of the loop. If the substring is empty, the function returns 0.