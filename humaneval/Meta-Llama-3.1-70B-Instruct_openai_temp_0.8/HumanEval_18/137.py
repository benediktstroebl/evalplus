```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring is found in the string.
    """
    if not substring:  # edge case: substring is empty
        return 0

    count = 0
    start = 0

    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # move the start position to the next character
        else:
            break

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines the `how_many_times` function, which takes two strings as input and returns the number of times the `substring` can be found in the `string`. The function uses a while loop to iterate over the string, and the `find` method to search for the substring. If the substring is found, the count is incremented and the start position is moved to the next character. The function returns the count.

The script also includes three test cases to verify the correctness of the function.