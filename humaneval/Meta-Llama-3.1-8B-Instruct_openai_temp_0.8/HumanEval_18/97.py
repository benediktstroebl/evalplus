### Solution: Counting Overlapping Substring Occurrences

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
    if not substring:  # edge case: empty substring
        return 0

    string_len = len(string)
    substring_len = len(substring)

    for i in range(string_len):
        # Check if the substring matches the string at the current index
        if string[i:i + substring_len] == substring:
            count += 1

    return count
```

### Example Usage:

```python
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This solution works by iterating over the original string and checking for a match at each position. It keeps a count of the number of matches and returns this count at the end. The edge case where the substring is empty is handled separately to avoid infinite loops.