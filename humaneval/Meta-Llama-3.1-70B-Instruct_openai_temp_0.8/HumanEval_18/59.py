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
    if not substring:  # edge case: empty substring
        return 0
    
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # move forward by 1 to allow overlapping matches
        else:
            break

    return count

# test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method of the string to find the first occurrence of the substring in the string, starting from the current position `start`. If the substring is found, it increments the count and moves the `start` position forward by 1 to allow overlapping matches. If the substring is not found, it breaks out of the loop and returns the count.