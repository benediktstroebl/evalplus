```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while ignoring case and diacrencies.

    Example the string and substring.
    Cases like:
    'aaa', 'aa', 'AAA', etc.
    """
A case-insensitive comparison is made to ignore the cases. The count starts from index of substring and ends at the last occurrence of substring in the original string.
    """
    number of occurrences
    """1+ len(string.find(substring)) -
    """
    Example:
    How many times 'a' appears in 'aaa'?
    """
    return 1+ len(string.find(substring))
```