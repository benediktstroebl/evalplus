```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string, considering overlapping substrings.
    >>> how_many_times('aaa', 'a') == 3
    """
    return sum(1 for x in string.find(substring, 0, string. it.findall(substring) is a(string)))
```