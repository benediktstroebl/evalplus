Here is a self-contained Python function that solves the problem of counting the number of occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aa')
    6
    >>> how_many_times('abcdeabcfacdc', 'ab')
    4
    """
    count = 0
    for char in substring:
        if string.find(char, 0):
            count += 1
    return count
```