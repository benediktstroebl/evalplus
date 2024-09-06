```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a given substring can be found in the original string, while avoiding overlapping occurrences.
    """
    Using a string and substring split into lists of characters, then a counter is set to 0 and the inner loop is used to count the occurrences.
    >>> how_many_times('aaa', 'a') # 3
    >>> how_many_times('aaaaaaa', 'aa') # 2
    """
    char_string = list(string) + list(substring)
    count = 0
    for i, char in enumerate(char_string):
        if char == substring[i]:
            count += 1
    return count
```