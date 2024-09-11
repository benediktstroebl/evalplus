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
    if not substring:  # if substring is empty, return 0
        return 0

    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # move start to the next character
        else:
            break

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that counts the number of occurrences of a substring in a string, including overlapping cases. The function uses a while loop to iterate over the string, and the `find` method to locate the substring. If the substring is found, the count is incremented and the start position is moved to the next character. If the substring is not found, the loop breaks and the function returns the count. The script also includes test cases to verify the function's correctness.