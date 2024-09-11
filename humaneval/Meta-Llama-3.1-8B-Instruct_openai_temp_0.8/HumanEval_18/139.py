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
    """
    if not substring:  # edge case: if substring is empty
        return 0

    count = 0
    for i in range(len(string)):
        if string.startswith(substring, i):  # check if substring matches at index i
            count += 1  # increment count if a match is found
    return count


# Example usage:
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a simple iterative approach to count the occurrences of the substring within the original string, including overlapping cases. It takes advantage of the `str.startswith()` method to check for matches at each position in the string. If the substring is found, it increments the count. At the end, it returns the total count.