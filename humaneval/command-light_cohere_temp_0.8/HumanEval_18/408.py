```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string. string if char == substring)

def test_how_many_times():
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcde', 'de') == 3
    assert how_many_times('abcba', 'a') == 2
    assert how_many_times('abcba', 'b') == 0
    assert how_many_times('xyabcdxy', 'abcd') == 4
    assert how_many_times('XYZ123XYZ', 'XYZ') == 3
```