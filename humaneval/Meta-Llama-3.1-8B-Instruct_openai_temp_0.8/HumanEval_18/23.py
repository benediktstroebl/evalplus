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
    if not substring:  # edge case: if the substring is empty
        return 0
    count = 0
    index = 0
    while index < len(string):  # keep searching until the end of the string
        index = string.find(substring, index)  # find the next occurrence
        if index!= -1:  # if a match is found
            count += 1  # increment the count
            index += 1  # move to the character after the match
        else:
            break  # if no match is found, stop searching
    return count

# test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the built-in `find` method of Python strings to search for the substring in the original string. It keeps track of the index where the search starts and increments the count for each match found. The `while` loop continues until the `find` method returns `-1`, indicating that the substring is no longer found in the string. The edge case where the substring is empty is handled by returning `0` immediately.