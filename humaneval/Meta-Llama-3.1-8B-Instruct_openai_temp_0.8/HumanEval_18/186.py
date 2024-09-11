```markdown
### How Many Times a Substring Can be Found in a String
#### Problem Description
Find how many times a given substring can be found in the original string. Count overlapping cases.

#### Solution
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the original string.

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    if not substring:  # Edge case: if the substring is empty
        return 0

    string_length, substring_length = len(string), len(substring)
    for i in range(string_length - substring_length + 1):
        # Check if the substring matches from the current position
        if string[i:i + substring_length] == substring:
            count += 1

    return count
```

#### Example Usage
```python
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

#### Commit Message
`Added how_many_times function to count overlapping occurrences of a substring in a string`