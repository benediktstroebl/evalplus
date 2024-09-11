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
    if len(substring) == 0:
        # If the substring is empty, return 0 because there can't be any matches
        return 0

    count = 0
    index = 0

    while index < len(string):
        # Find the index of the substring in the string starting from the current position
        index = string.find(substring, index)

        # If the substring was not found, break out of the loop
        if index == -1:
            break

        # Increment the count and move the index to the position right after the matched substring
        count += 1
        index += 1

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

In this script, we use the `find` method of the string to find the index of the substring. We start searching from the current position (`index`) and increment `index` by 1 after each match to avoid counting the same match multiple times. If `find` returns `-1`, it means the substring was not found, and we break out of the loop.