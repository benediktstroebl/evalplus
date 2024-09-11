```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string.
    Counts overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    if not substring:
        return 0  # If substring is empty, return 0
    count = 0
    string_len = len(string)
    substring_len = len(substring)
    
    # Iterate over the string
    for i in range(string_len):
        # Check if the substring matches the current position in the string
        if string[i:i + substring_len] == substring:
            count += 1
    
    return count

# Test cases
if __name__ == "__main__":
    print(how_many_times('', 'a'))  # 0
    print(how_many_times('aaa', 'a'))  # 3
    print(how_many_times('aaaa', 'aa'))  # 3
```

This code defines the `how_many_times` function as specified. It iterates over the string, checking for matches of the substring at each position. The `if not substring` check handles the edge case where the substring is empty. The test cases at the end demonstrate the function's behavior.