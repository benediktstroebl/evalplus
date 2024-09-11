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

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # Handle the edge case where the substring is empty
    if not substring:
        return 0

    # Use a generator expression to generate the indices of all occurrences
    # of the substring in the string
    indices = (i for i in range(len(string)) if string.startswith(substring, i))

    # Sum up the number of indices
    count = sum(1 for _ in indices)

    return count

# Test the function
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This script defines the `how_many_times` function that takes a string and a substring as input and returns the number of times the substring appears in the string, counting overlapping cases. It uses a generator expression to generate the indices of all occurrences of the substring and sums up the number of indices to get the count. The script also includes test cases to demonstrate the function's behavior.