```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Parameters:
    string (str): The original string.
    substring (str): The substring to be searched.

    Returns:
    int: The number of times the substring can be found in the string.
    """
    count = 0
    length = len(substring)
    for i in range(len(string) - length + 1):
        if string[i:i + length] == substring:
            count += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a simple loop to iterate over the string, checking each substring of the same length as the given substring. If a match is found, it increments the count. This approach counts overlapping cases, as required. The script also includes test cases to verify its correctness.