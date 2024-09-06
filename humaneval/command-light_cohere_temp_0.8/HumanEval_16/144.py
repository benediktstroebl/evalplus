```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha() and string andc})

def test_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
```