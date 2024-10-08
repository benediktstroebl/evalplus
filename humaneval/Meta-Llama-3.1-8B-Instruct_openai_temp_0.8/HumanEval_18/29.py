```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be searched.

    Returns:
    int: The number of times the substring can be found in the original string.
    """
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

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find()` method of the string class to search for the substring. The `find()` method returns the index of the first occurrence of the substring, or -1 if it is not found. The script continuously calls `find()` with the next index as the start position until it cannot find the substring anymore. The count of successful searches is returned.