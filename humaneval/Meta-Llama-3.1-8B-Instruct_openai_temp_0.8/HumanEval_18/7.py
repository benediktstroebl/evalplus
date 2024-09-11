```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the original string.
    """
    if len(substring) == 0:  # edge case: if substring is empty
        return 0
    count = 0
    index = 0
    while index < len(string):  # loop through the string
        index = string.find(substring, index)  # find the substring in the string, starting from index
        if index!= -1:  # if the substring is found
            count += 1  # increment the count
            index += 1  # move the index to the right of the found substring
        else:
            break  # if the substring is not found, break the loop
    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```