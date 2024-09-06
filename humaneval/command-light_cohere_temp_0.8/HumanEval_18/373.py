```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, overlapping instances allowed.
    >>> how_many_times('aaaa', 'aa')  # Output: 3
    >>> how_many_times('abcdeabcba', 'abc')  # Output: 3
    >>> how_many_times('abcdeabcba', 'ab')  # Output: 2
    >>> how_many_times('abcdeabcba', 'bcde')  # Output: 0
    >>> how_many_times('abcdeabcba', 'xyxzz')  # Output: 0
    """
    counter = 0
    for char in substring:
        if char in string:
            counter += 1
    return counter
```