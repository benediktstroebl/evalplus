```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping occurrences.
    >>> Returns: empty string
    >>> how_many_times("", "")
    0
    >>> how_many_times("ab..." , "a")
    2
    >>> how_many_times("abcdefg", "abc")
    4
    >>> how_many_times("aa", "a")
    0
    """
    count = 0
    start = 0
    current = substring
    while current != "" and start <= len(string):
        if string[start] == current:
            start += 1
        else:
            count += 1
        current = substring if current[-1] != "" else ""
    return count
```