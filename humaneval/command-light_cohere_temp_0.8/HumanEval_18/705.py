Here is a self-contained Python script that solves the problem of counting occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('abcde', 'de') # returns 5
    """
    count = 0
    string = str.replace(string, substring)
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```