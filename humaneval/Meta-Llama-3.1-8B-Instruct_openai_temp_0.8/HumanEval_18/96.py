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
    count = 0
    i = 0  # Start index

    # Continue searching for the substring until we've searched the entire string
    while i < len(string):
        # Find the index of the substring in the string, starting from the current index
        index = string.find(substring, i)

        # If the substring was found, increment the count and move the start index to the end of the found substring
        if index!= -1:
            count += 1
            i = index + 1
        # If the substring was not found, we've reached the end of the string, so break the loop
        else:
            break

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```