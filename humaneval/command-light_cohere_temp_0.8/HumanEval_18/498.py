```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('abcda', 'abc')
    2
    >>> how_many_times('abcdaaaa', 'abc')
    3
    >>> how_many_times('abcdaaaa', 'aaa')
    0
    """
    return sum((1 for i, c in enumerate(string) if c == substring))

# Test
def test():
    assert how_many_times('abcdaaaa', 'aaa') == 0
test()
```