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
    count = 0
    if not substring:
        return count
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string, counting overlapping cases. It uses a simple loop to iterate over the string, checking each position to see if the substring starts there. If it does, it increments the count. At the end, it returns the count.

You can test the function with the provided examples to see that it works correctly.