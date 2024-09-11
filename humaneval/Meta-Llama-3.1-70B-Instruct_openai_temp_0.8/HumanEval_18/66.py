```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring can be found.
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
print(how_many_times('', 'a'))  # Expected: 0
print(how_many_times('aaa', 'a'))  # Expected: 3
print(how_many_times('aaaa', 'aa'))  # Expected: 3
```