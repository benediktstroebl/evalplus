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

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not string or not substring:
        return 0

    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```
This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string, counting overlapping cases. It does this by iterating over the string and checking if the substring matches at each position. If a match is found, the count is incremented. The function returns the total count.