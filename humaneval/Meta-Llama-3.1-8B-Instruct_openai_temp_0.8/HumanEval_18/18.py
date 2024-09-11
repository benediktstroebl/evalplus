```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring occurs in the string.
    """
    if not substring:  # edge case: substring is empty
        return 0

    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes two parameters, `string` and `substring`. It then iterates over the `string` and checks if the current character and the following characters match the `substring` using the `startswith` method. If they do, it increments the count. The function returns the count at the end. The edge case where the `substring` is empty is also handled by returning 0 immediately. The test cases are included at the end to verify the correctness of the function.