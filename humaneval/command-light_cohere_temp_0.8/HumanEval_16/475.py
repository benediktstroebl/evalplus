```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. strings.lower() if c in string})

def test_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('ABC') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
```