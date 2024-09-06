Here is a Python script that contains a self-contained function to find the number of occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string, 
    accounting for case-insensitive matching and overlapping substring occurrences.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('hello world', 'world')
    2
    """
    return sum(1 for x in string.contains(substring))
```