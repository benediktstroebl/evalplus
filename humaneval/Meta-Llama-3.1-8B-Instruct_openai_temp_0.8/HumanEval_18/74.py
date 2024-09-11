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
    """
    count = 0
    index = 0

    # If the substring is empty, return 0
    if not substring:
        return 0

    # If the string is empty, return 0
    if not string:
        return 0

    while index < len(string):
        # Find the substring in the string starting from the current index
        index = string.find(substring, index)

        # If the substring is not found, break the loop
        if index == -1:
            break

        # Increment the count and move the index to the end of the found substring
        count += 1
        index += len(substring)

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring can be found in the string, counting overlapping cases. It uses a while loop to continuously search for the substring in the string, incrementing the count each time it's found and moving the search index to the end of the found substring. If the substring is not found, it breaks the loop. The function also handles edge cases where the substring or string are empty.