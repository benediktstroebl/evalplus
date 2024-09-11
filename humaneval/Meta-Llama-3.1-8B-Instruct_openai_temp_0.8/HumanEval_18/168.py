```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring appears in the string.
    """
    count = 0
    i = 0
    while i < len(string):
        i = string.find(substring, i)
        if i!= -1:
            count += 1
            i += 1
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses Python's built-in `str.find()` method to find the index of the substring within the string. If the substring is found, it increments the count and moves the index forward by 1 to prevent finding the same match again. This process continues until the substring is no longer found in the string. The function then returns the count of times the substring appears in the string.