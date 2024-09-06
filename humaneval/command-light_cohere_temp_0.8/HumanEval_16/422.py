```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.org if c.isalpha()})

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
```