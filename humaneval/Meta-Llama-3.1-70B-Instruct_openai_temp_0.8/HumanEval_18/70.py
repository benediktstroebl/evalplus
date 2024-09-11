```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
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

    # Handle edge case where the substring is empty
    if len(substring) == 0:
        return 0

    # Use a generator expression with the enumerate function to generate indices
    # of the substring in the string. The start parameter is used to account for
    # overlapping matches.
    matches = (i for i in range(len(string)) if string.startswith(substring, i))

    # Use the sum function to count the number of matches
    return sum(1 for _ in matches)


# Test the function
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```