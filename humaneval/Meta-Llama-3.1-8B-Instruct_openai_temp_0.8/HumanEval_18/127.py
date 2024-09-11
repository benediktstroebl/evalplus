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
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1  # Move to the next character to find the next occurrence
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method of the string class to search for the substring in the string, starting from the current index. If the substring is found, it increments the count and moves to the next character to find the next occurrence. The loop continues until the substring is not found anymore. The result is the total count of occurrences.