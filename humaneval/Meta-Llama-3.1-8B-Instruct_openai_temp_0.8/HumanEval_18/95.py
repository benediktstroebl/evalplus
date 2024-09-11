```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring appears in the string.
    """
    if not string or not substring:
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

This script defines a function `how_many_times` that takes two parameters: `string` and `substring`. It then uses a while loop to find all occurrences of `substring` in `string`, counting overlapping cases. If `substring` is not found after starting at a given position, the loop breaks and the function returns the count. The function handles edge cases where either `string` or `substring` is empty by returning 0 in these cases.