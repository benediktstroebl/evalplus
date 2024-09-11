```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0
    if not substring:
        return count  # If the substring is empty, return 0
    for i in range(len(string) + 1 - len(substring)):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string, counting overlapping cases. It uses a simple loop to check each substring of the same length as the given substring, and increments a counter whenever a match is found. The test cases at the end demonstrate the function's behavior.