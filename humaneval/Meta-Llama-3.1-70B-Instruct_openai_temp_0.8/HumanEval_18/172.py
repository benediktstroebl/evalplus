```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring is found in the string.
    """
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # move the start pointer to the next character
        else:
            break

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring appears in the string, including overlapping cases. The function uses the `find` method of the string class to find the position of the substring in the string, starting from a given position. If the substring is not found, the `find` method returns -1, and the function breaks out of the loop. Otherwise, the function increments the count and moves the start pointer to the next character. The function returns the count at the end.

The script also includes test cases to verify that the function works correctly.