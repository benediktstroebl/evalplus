```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string, including overlapping cases.
    """
    if not substring:  # Edge case: empty substring
        return 0
    index = 0
    count = 0
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        count += 1
        index += len(substring)
    return count
```