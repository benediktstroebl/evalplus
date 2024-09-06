Here is a Python script that defines a function to solve the problem you have provided:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aa', 'a') == 0
    >>> how_many_times('aaaaaa', 'aa') == 6
    """
    return sum(1 for i, x in enumerate(string.find(substring)))
```