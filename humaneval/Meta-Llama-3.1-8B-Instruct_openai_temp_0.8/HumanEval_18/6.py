```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1  # Move the index to the next character to avoid overlapping matches
        else:
            break
    return count
```

This script defines a function `how_many_times` that takes two string arguments, `string` and `substring`, and returns the number of times `substring` appears in `string`, allowing for overlapping matches. The function uses a while loop to continuously search for `substring` in `string`, starting from the current index, and increments the count and index accordingly. If `substring` is not found, the loop breaks and the count is returned.