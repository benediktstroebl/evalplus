Here is a self-contained Python script that defines a function to solve the problem of finding the number of times a substring can be found in a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaaaaa', 'a')
    3
    """
    return len(string.find(substring))
```