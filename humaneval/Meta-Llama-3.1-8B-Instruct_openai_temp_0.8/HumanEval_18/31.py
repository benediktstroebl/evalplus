### Substring Counting in a String
#### Problem Description

This script counts the number of times a given substring appears in a string, including overlapping occurrences.

#### Code

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

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    # Iterate over the string with a sliding window of the substring's length
    for i in range(len(string) - len(substring) + 1):
        # Check if the current window matches the substring
        if string[i:i + len(substring)] == substring:
            # If it does, increment the count
            count += 1
    return count

# Example usage
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

#### Explanation

This script works by iterating over the original string with a sliding window of the substring's length. For each window, it checks if the substring matches the current window. If it does, it increments the count. This process is repeated until the end of the string is reached, at which point the count is returned as the result.