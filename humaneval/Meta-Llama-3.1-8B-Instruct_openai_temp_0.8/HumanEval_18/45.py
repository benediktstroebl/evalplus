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
    if not substring:  # Edge case: If substring is empty, return 0
        return 0
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)  # Find the substring in the string starting from the current index
        if index!= -1:  # If the substring is found
            count += 1
            index += 1  # Move the index to the position right after the found substring
        else:
            break  # If the substring is not found, break the loop
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines the `how_many_times` function, which takes a string and a substring as arguments. It then uses a while loop to continuously search for the substring in the string, starting from the current index. The `find` method is used to find the substring in the string, and the `+ 1` is used to move the index to the position right after the found substring. The loop continues until the substring is not found. The function returns the count of found substrings.