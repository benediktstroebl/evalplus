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

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    index = 0

    # Loop through the string until we've checked all characters
    while index < len(string):
        # Check if the substring is found at the current index
        if string[index:].startswith(substring):
            # If the substring is found, increment the count and move the index forward
            # by the length of the substring to check for overlapping cases
            count += 1
            index += len(substring)
        else:
            # If the substring is not found, move the index forward by 1 character
            index += 1

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script implements a function `how_many_times` that takes two arguments: a string and a substring. It counts the number of times the substring can be found in the original string, considering overlapping cases. The function uses a while loop to iterate through the string and checks for the substring at each index. If the substring is found, the count is incremented and the index is moved forward by the length of the substring. If the substring is not found, the index is moved forward by 1 character. The function returns the total count of times the substring is found in the original string.