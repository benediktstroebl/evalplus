```python
def how_many_times(string: str, substring: str) -> int:
    """
    This function returns the number of times the given substring can be found in the original string.
    """
    strings which only contains alpha characters and the substring is 'a'.
    return sum(1 for c in string if c == substring)
    """
def test_how_many_times():
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaaaa', 'a') == 6
    assert how_many_times('abcde', 'de') == 3
    assert how_many_times('ABCDEF', 'A') == 5
    assert how_many_times(' ABCDEF ', 'A') == 5
    assert how_many_times('abcba', 'b') == 2
    assert how_many_times('Testing', 'eting') == 0
```