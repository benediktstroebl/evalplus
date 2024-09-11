```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    if not substring:
        return 0  # Empty substring cannot be found in any string

    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:  # Found the substring
            count += 1
            index += 1  # Move to the position right after the found substring
        else:
            break  # Substring not found, exit the loop

    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script defines a function `how_many_times` that takes two string parameters: `string` and `substring`. It counts how many times the `substring` appears in the `string`, including overlapping cases, and returns this count as an integer. The script includes test cases to verify the function's correctness.