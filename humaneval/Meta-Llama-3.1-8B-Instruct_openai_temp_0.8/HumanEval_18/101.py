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
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    index = 0

    # Loop until the substring is no longer found in the string
    while True:
        index = string.find(substring, index)
        if index!= -1:  # substring found
            count += 1
            index += 1  # move the search position one character forward
        else:
            break

    return count

# Example use cases:
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a `while` loop to continuously search for the substring in the original string, starting from the current index. It counts each occurrence and moves the search position forward by one character after finding a match. The loop stops when the substring is no longer found in the string. The result is the total count of occurrences.