Here is a self-contained Python script that solves the problem of counting the frequency of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the frequency of a given substring within the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('hello world', 'world')
    0
    >>> how_many_times('hello world', 'hello')
    1
    """
    return len(string.find(substring))
```