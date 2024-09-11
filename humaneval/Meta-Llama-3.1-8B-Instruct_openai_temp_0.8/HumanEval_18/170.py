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

    Example:
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
        index = string.find(substring, index)  # start searching from the current index
        if index == -1:  # substring not found
            break
        count += 1
        index += 1  # move the index to the next character
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method of the string class in Python, which returns the index of the first occurrence of the substring. If the substring is not found, it returns -1. The loop continues to search for the substring until it's found no more times. The index is incremented by 1 after finding a substring to ensure overlapping cases are counted.