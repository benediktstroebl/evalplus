Here's a self-contained Python function that returns the count of occurrences of a given substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('abcde', 'abcd')
    4
    >>> how_many_times('abcba', 'abc')
    2
    """
    return sum(1 for x in string.find(substring, 0, string.how_many_times(substring, substring)))
```