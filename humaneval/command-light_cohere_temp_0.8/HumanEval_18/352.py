Here is a self-contained Python script with a function that solves the problem you described:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping occurrences.
    >>> string: Input string
    >>> substring: Input substring
    >>> string: Input string
    >>> self.find_many_times(string, substring)
    <number>
    """
    count = 0
    length = len(string)
    i, j = 0, 0
    while i < length:
        while j >= 0 and string[i] == substring[j]:
            j -= 1
        if j == -1:
            count += 1
        i += 1
        if i >= length:
            break
    return count
```