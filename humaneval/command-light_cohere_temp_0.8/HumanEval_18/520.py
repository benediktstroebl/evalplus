```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')  # Output: 3
    >>> how_many_times('aaaa', 'aa')  # Output: 3
    >>> how_many_times('abcdeabcdeabc', 'abc')  # Output: 4
    """
    return len(string) // (len(substring) + 1)
```