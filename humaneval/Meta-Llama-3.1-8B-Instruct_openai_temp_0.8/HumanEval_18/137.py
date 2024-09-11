```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring appears in the string.
    """
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1  # Move index forward to avoid counting the same match again
        else:
            break
    return count

# Example use cases:
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This script uses the `find` method to locate the substring within the string, and increments the count each time a match is found. If no match is found, the `find` method returns -1, which triggers the `break` statement to exit the loop. The script also increments the index by 1 after each match to avoid counting the same match again, effectively allowing for overlapping matches.