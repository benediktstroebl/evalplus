```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0
    if not substring:  # If the substring is empty, return 0
        return 0
    for i in range(len(string)):
        if string[i:].startswith(substring):  # Check if the substring starts with the remaining string
            count += 1
    return count


# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script defines a function `how_many_times` that takes a string and a substring as input. It then iterates over the string, checking if the substring starts with the remaining string in each position. If the substring starts with the remaining string, it increments the count. Finally, it returns the count. If the substring is empty, it returns 0 immediately. The test cases at the end demonstrate the function's correctness.