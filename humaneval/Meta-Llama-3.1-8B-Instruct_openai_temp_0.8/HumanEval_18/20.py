```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.
    """
    count = 0
    index = 0

    # Continue searching for the substring as long as there are still characters in the string
    while index < len(string):
        # Find the index of the substring in the string, starting from the current index
        index = string.find(substring, index)

        # If the substring is not found, find() returns -1, so we exit the loop
        if index == -1:
            break

        # Increment the count and move the index to the position right after the found substring
        count += 1
        index += 1

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```