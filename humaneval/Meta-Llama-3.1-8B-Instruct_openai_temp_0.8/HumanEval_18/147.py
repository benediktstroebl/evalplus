```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of occurrences of the substring in the string.
    """
    if not substring:
        return 0  # edge case: if substring is empty, return 0

    count = 0
    i = 0
    while i < len(string):
        i = string.find(substring, i)
        if i!= -1:
            count += 1
            i += 1  # move the index to the next character
        else:
            break

    return count


# Example usage:
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

In this solution, we use the built-in `str.find()` method to search for the substring in the string. The `find()` method returns the index of the first occurrence of the substring, or -1 if it's not found. We use a while loop to keep searching for the substring starting from the current index. The index is incremented by 1 each time the substring is found, to account for overlapping cases. If the substring is not found, we break out of the loop.