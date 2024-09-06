```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    """: Returns a function takes two arguments, string and substring, and returns the number of occurrences of the substring in the string.
    """
    for i, j in string:
        if j in substring:
            return i + 1
    return 0
```