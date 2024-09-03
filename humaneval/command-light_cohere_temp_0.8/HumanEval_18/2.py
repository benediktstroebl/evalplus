```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string.
    Counting only the
 overlapping case.
    Returns 0 if substring is not found and substring length is 1.
    """
    first_match = string.find(substring)
    if first_match == -1:
        return 0

    count = 1
    while string[first_match:].find(substring) != -1:
        first_match += 1
        count += 1

    return count
```