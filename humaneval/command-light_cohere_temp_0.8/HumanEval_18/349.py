```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    including overlapping occurrences.
    Return the count.
    """
    how many: 
    -1
    """
    return len([i for i, j in zip(string.find(substring, 0), range(len(string))))])
def test_how_many_times():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
```