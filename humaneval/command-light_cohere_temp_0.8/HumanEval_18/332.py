Here's the self-contained Python script that defines and implements a function to solve the problem you described:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, counting overlapping matches.
    >>> how_many_times('aaa', 'a')  # returns 3
    >>> how_many_times('aaaaaaa', 'aaa')  # returns 3
    """
    return len([i == substring for i, sub in enumerate(string)])
```