```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    if not substring:  # edge case: empty substring
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

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string, counting overlapping cases. The function uses a while loop to search for the substring, starting from the current position each time. If the substring is found, the count is incremented and the search starts from the next character. If the substring is not found, the loop breaks. The function also handles the edge case where the substring is empty.

The script includes test cases at the end to verify that the function works correctly.