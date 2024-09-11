```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring is found in the string.

    Examples:
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
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1
        else:
            break

    return count


import doctest
doctest.testmod()
```

This script defines the `how_many_times` function, which finds the number of times a given substring is found in the original string, counting overlapping cases. The function iterates over the string, finding the position of the substring and incrementing the count each time it is found. If the substring is not found, the function breaks out of the loop.

The script also includes a docstring that provides documentation for the function, including examples of how to use it. The `doctest.testmod()` function is used to test the function with the examples provided in the docstring.