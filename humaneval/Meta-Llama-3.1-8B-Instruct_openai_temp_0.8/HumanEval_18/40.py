```markdown
### Counting Substring Occurrences

This script defines a function `how_many_times` that finds the number of occurrences of a given substring within a string, including overlapping cases.

#### Code

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of occurrences of the substring.

    Example:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count
```

#### Usage

You can use this function like this:
```python
print(how_many_times('hello world', 'o'))  # Output: 2
print(how_many_times('abcabcabc', 'abc'))  # Output: 3
```
This code takes advantage of Python's string slicing and `str.startswith` method to efficiently find all occurrences of the substring. The loop iterates over the string, checking each position to see if the substring can be found starting at that position. If it can, the count is incremented by 1. The function then returns the total count of occurrences.