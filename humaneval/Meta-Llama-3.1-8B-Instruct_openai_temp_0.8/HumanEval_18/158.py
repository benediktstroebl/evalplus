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

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    if len(substring) == 0:
        return 0
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1
        else:
            break
    return count
```

This script defines the `how_many_times` function, which takes two string arguments, the original string and the substring to search for. It then uses a loop to find all occurrences of the substring in the string, incrementing the count each time a match is found. The function uses the `find` method of Python's string class to search for the substring, which returns the index of the first occurrence of the substring. If no match is found, `find` returns -1. The loop continues until all characters in the string have been checked. The function returns the total count of times the substring appears in the string.