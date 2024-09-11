```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    if not substring:  # Edge case: if the substring is empty, return 0
        return 0

    count = 0
    start = 0

    while start < len(string):
        pos = string.find(substring, start)  # Find the substring in the string, starting from the current position
        if pos!= -1:  # If the substring is found
            count += 1
            start = pos + 1  # Move the start position to the character after the found substring
        else:
            break  # If the substring is not found, break the loop

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes two string arguments, `string` and `substring`, and returns the number of times `substring` can be found in `string`, counting overlapping cases. The function uses a loop to find all occurrences of `substring` in `string`, incrementing the count each time a match is found. If the substring is not found, the loop breaks, and the function returns the count. The script includes test cases to verify the function's correctness.