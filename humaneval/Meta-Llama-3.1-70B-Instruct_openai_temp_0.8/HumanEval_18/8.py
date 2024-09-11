```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    if not substring:  # edge case: substring is empty
        return 0

    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            start = pos + 1
            count += 1
        else:
            break

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a simple iterative approach with the `find` method to locate the substring within the string, incrementing the count and the start position each time a match is found. If no match is found, the loop breaks and the count is returned.