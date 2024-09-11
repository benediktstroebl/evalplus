```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Counting overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    count = 0
    substring_length = len(substring)
    string_length = len(string)

    for i in range(string_length):
        # Check if the substring matches at the current position
        if string[i:i + substring_length] == substring:
            count += 1

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This Python script implements the `how_many_times` function, which counts the number of times a given substring can be found in a string, including overlapping cases. The function iterates over the string and checks if the substring matches at each position. If a match is found, it increments the count. The test cases at the end demonstrate the function's behavior for different inputs.