```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string.
    >>> how_many_times('aaaaaa', 'a')  # Output: 6
    """
    count = 0
    string = string.replace(substring)
    for i in range(len(string) - len(substring) + 1)):
        if string[:i] == substring:
            count += 1
    return count
```