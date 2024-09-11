```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring is found in the string.
    """
    count = 0
    start = 0
    while True:
        start = string.find(substring, start)
        if start!= -1:
            count += 1
            start += 1  # Move to the next character to find overlapping substrings
        else:
            return count

# Example use cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```