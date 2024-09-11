```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of occurrences of the substring in the string.
    """
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # move start position to the next character
        else:
            break

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of occurrences of the substring in the string. The function uses the `find` method to search for the substring in the string, and it moves the start position to the next character after each match to count overlapping cases. The test cases at the end of the script verify that the function works correctly.