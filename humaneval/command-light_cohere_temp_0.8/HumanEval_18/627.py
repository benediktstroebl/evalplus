```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts the number of occurrences of a given substring within the original string.
    """
    check:
        return 0 if substring not in string
        return len([char for char in substring if char in string])
    
    """
    return check()

def test_how_many_times():
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcde', 'de') == 2
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcabc', 'a') == 4
    assert how_many_times('abcabc', 'b') == 1
    assert how_many_times('abcabc', 'ab') == 2
    assert how_many_times('abc', 'a') == 0
```