```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})

def test_distinct_characters() -> None:
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('JER') == 4
    assert count_distinct_characters('hello world!') == 6
    assert count_distinct_characters('123') == 4
    assert count_distinct_characters('abcXylolo') == 5
    assert count_distinct_characters(' ') == 0
    assert count_distinct_characters('') == 1
    
    return None
```