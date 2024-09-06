Here's the code:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string, accounting for case-overlap.

    Parameters:
        string: The input string
        substring: The substring to find
    Returns: count: The number of occurrences of the substring in the string
"""
    string = 'aaaa' + 'a' + 'aaaa'
    return len(string.replace(substring))
```