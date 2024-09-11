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
    count = 0
    string_length = len(string)
    substring_length = len(substring)

    # Handle edge case where substring is empty
    if substring_length == 0:
        return string_length + 1

    # Handle edge case where substring is longer than the string
    if substring_length > string_length:
        return 0

    for i in range(string_length - substring_length + 1):
        if string[i:i + substring_length] == substring:
            count += 1

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the original string. The function handles edge cases where the substring is empty or longer than the string. It uses a loop to iterate over the original string and checks if the substring matches at each position. The count of matches is then returned.