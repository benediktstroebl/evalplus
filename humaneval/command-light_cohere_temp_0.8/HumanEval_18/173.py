Here is a self-contained Python script that solves the problem of counting occurrences of a substring in a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('abcdeabcde', 'abcde')
    5
    >>> how_many_times('abcdaaadd', 'aaa')
    0
    """
    return sum((1 for char in substring if char in string))
```