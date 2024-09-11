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
    count = 0
    i = 0
    while i < len(string):
        i = string.find(substring, i)
        if i!= -1:
            count += 1
            i += 1  # Move the start of the search one character after the found substring
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a while loop to find the substring in the string, starting from the current position `i`. If the substring is found, the count is incremented and `i` is moved one character after the found substring. If the substring is not found, the loop breaks.