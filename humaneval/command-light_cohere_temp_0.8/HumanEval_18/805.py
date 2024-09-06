Here is a self-contained Python script that defines a function to solve the problem of finding the number of times a given substring can be found in a string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')  # Should return 3
    >>> how_many_times('aaaaaaa', 'aa')  # Should return 6
    """
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count
```