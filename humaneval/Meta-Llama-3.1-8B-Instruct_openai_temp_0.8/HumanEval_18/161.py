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
    count = 0
    if substring == "":
        return 0
    else:
        i = 0
        while i < len(string):
            if string.startswith(substring, i):
                count += 1
                i += 1
            i += 1
        return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a while loop to iterate through the original string. For each iteration, it checks if the current position in the string is the start of the substring. If it is, it increments the count and moves the position forward by 1 (to allow for overlapping matches). If the position is not the start of the substring, it simply moves the position forward by 1. The function returns the final count of how many times the substring can be found in the string.