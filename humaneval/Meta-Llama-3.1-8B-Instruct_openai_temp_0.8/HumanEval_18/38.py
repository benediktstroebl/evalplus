### Substring Frequency Counter
#### Python Script

```markdown
### Code

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring occurs in the string.
    """
    count = 0
    if not substring:
        return count  # Edge case: if substring is empty, return 0

    string_len = len(string)
    substring_len = len(substring)

    for i in range(string_len - substring_len + 1):  # Iterate over possible positions
        if string[i:i + substring_len] == substring:
            count += 1  # Found a match, increment count

    return count
```

### Example Use Cases

```python
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring occurs in the string, counting overlapping cases. The function uses a loop to iterate over possible positions in the string and checks if the substring matches at each position. If a match is found, the count is incremented. The function returns the final count.