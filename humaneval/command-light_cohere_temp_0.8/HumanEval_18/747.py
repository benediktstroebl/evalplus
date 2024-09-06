```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test the function
def test_how_many_times():
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcde', 'abc') == 4
    assert how_many_times('abcba', 'ab') == 3
    assert how_many_times('abcbb', 'ab') == 4
    assert how_many_times('abcba', 'ab') != 5
```