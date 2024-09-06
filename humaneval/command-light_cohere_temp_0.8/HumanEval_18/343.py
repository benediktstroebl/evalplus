Here's a self-contained Python script with a function that finds the number of occurrences of a given substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of times a given substring can be found in the original string.
    >>> how_many_times('aaaaaa', 'aa')  # Output: 3
    """
    return len([i for i, c in enumerate(string) if c == substring])
```