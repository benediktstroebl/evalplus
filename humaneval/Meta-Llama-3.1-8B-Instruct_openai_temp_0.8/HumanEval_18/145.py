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
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            start = pos + 1
            count += 1
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a while loop to continuously find the position of the substring in the string, starting from the position where the last match was found (or the start of the string if it's the first time). If a match is found, it increments the count and moves the start position to the position right after the match. If no match is found, it breaks out of the loop. This effectively counts overlapping cases.