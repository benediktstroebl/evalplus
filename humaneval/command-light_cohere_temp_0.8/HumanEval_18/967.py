```python
def how_many_times(string: str, substring: str) -> int:
    """
    Returns the number of times the substring can be found in the original string.
    """
    strings are same substring, return 1.
    if not substring in string:
        return 0

    counter = 0
    i = len(string) - 1
    while i >= 0:
        if string[i] == substring:
            counter += 1
            i -= 1
        i -= 1

    return counter
```