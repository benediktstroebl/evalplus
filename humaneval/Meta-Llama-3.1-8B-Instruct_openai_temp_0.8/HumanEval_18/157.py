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
    if len(substring) == 0:
        return count
    
    string_length = len(string)
    substring_length = len(substring)
    
    for i in range(string_length):
        if string[i:i + substring_length] == substring:
            count += 1
    
    return count

# Test cases
print(how_many_times("", "a"))  # Expected: 0
print(how_many_times("aaa", "a"))  # Expected: 3
print(how_many_times("aaaa", "aa"))  # Expected: 3
```

This Python script defines a function `how_many_times` that counts the number of occurrences of a substring within a given string, considering overlapping cases. The function iterates through the original string and checks for matches with the substring. If a match is found, the count is incremented. The function returns the final count. The test cases are included at the end to demonstrate the function's behavior.