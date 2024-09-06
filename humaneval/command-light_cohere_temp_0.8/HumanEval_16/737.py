```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.app.lowercase = c.isdigit() for c})
```

def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XyX') == 2
    assert count_distinct_characters('jerry') == 4
```