```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring can be found in the original string.

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
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
print(how_many_times('', 'a'))
print(how_many_times('aaa', 'a'))
print(how_many_times('aaaa', 'aa'))
```

This script uses the built-in `str.find()` method, which returns the index where the substring is found in the string, or -1 if it's not found. We use the `while` loop to continuously find the substring in the string, starting from the last position of the previous match. If a match is found, we increment the count and the index, otherwise we break the loop.