```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    if not substring:
        # If the substring is empty, it can be found at any position in the string.
        return len(string) + 1
    count = 0
    i = 0
    while i < len(string):
        # Find the substring at the current position.
        i = string.find(substring, i)
        if i == -1:
            # If the substring is not found, break the loop.
            break
        count += 1
        # Move to the position right after the found substring.
        i += len(substring)
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```