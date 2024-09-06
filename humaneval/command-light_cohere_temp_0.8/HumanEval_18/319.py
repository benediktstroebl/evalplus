```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find how many times a given substring can be found in the original string.
    Count overlapping cases.
    """ A code:
    return sum(1 for c in string.sub.find(substring, len(string))
    """
def test_function():
    assert how_many_times("aaa", "a") == 3
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abc", "ab") == 2
    assert how_many_times("aa", "a") == 0
    assert how_many_times("ababc", "ab") == 2
```