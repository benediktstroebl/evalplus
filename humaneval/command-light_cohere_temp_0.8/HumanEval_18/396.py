Here is a self-contained Python script that defines a function `how_many_times`, which calculates the number of occurrences of a given substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')  # Output: 3
    """
    return sum(1 for s in string.find(substring, 0, len(substring)))
```