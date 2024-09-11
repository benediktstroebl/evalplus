**Substring Counting**
======================

### Description

This script provides a function `how_many_times` to count the occurrences of a given substring within a string. It includes overlapping cases in the count.

### Code
```markdown
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
    if not substring:  # Edge case: empty substring
        return 0
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):  # Check for substring at current index
            count += 1
    return count
```

### Example Use Cases

```python
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```