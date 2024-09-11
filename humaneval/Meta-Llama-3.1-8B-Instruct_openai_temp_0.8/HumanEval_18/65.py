```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

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
    if not substring:
        return 0
    
    string_len = len(string)
    substring_len = len(substring)

    for i in range(string_len - substring_len + 1):
        if string[i:i + substring_len] == substring:
            count += 1

    return count
```

This script defines a function `how_many_times` that takes two arguments: the original string and the substring to search for. It returns the number of times the substring can be found in the original string, including overlapping cases. The function uses a simple loop to iterate over the original string and check if the substring matches at each position. If the match is found, it increments the count. Finally, it returns the count.