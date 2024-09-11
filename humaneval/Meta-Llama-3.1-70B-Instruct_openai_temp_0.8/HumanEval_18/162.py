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
    """
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    i = 0
    while i < len(string):
        if string[i:i + len(substring)] == substring:
            count += 1
        i += 1

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines the `how_many_times` function as specified. It uses a simple iterative approach to count the occurrences of the substring in the original string, including overlapping cases. The function handles the edge case where the substring is empty, returning 0 in this case. The script also includes the provided test cases to verify the correctness of the function.