```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    Return the string.over and substring.
    Count all occurrences of the maxes to 1 and adds them up.
    """
    over a maximum of substring length.
    """
```
def test_how_many_times():
    assert how_many_times("aaaaaa", "aa") == 3
    assert how_many_times("Hello", "ll") == 2
    assert how_many_times("""hELLo""", "ll") == 4
    assert how_many_times("Python", "Is") == 1
    assert how_many_times("Python", "ple$$") == 0
    assert how_many_times("", "p") == 0
```