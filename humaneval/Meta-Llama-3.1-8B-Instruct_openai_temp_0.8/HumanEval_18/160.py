```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the original string.

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count
```

This script defines a function `how_many_times` that calculates how many times a given `substring` appears in a given `string`. It uses a for loop to iterate over the string, checking if the substring appears at each position. If it does, it increments the count. This solution correctly counts overlapping cases, meaning that if the substring appears multiple times within the same part of the string, each instance is counted separately.