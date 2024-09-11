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
    # If the substring is empty or the string is empty, return 0
    if not substring or not string:
        return 0
    # If the substring is not empty and the string is not empty, use the count method with a start index of 0
    # This allows for overlapping matches to be counted
    else:
        count = 0
        start = 0
        while start < len(string):
            pos = string.find(substring, start)
            if pos!= -1:
                count += 1
                start = pos + 1
            else:
                break
        return count
```

You can test this function with the provided examples:
```python
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This function uses the `find` method to locate the substring in the string, starting at the current `start` index. If a match is found, it increments the count and moves the `start` index to the position after the match. This process continues until no more matches are found.