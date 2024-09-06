Here is a self-contained Python script with a function that solves the problem of finding how many times a given substring can be found in the original string, while accounting for overlapping cases:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.

    # Count the - string and substring split into individual characters
    char_list = list(string) + list(substring)

    # Count the occurrences of the substring in the original string
    occurrences = Counter(char_list)
    return occurrences.count(substring)
```