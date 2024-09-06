Here is a self-contained Python script that defines a function to solve the problem of counting the occurrences of a substring within a given string:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('123456', '123')
    4
    >>> how_many_times('abcdeabcde', 'abc')
    3
    """
    return sum(1 for char in substring if char in string)
```