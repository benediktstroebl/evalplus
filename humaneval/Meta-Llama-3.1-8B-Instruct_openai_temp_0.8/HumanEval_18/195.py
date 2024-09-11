```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    if not substring:  # edge case: if the substring is empty
        return 0
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):  # check if the substring starts at the current position
            count += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes two arguments: `string` and `substring`. It iterates over the `string` and checks if the `substring` starts at each position. If it does, it increments the count. Finally, it returns the count. The test cases at the end demonstrate the function's usage.