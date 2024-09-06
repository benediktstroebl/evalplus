```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.nameset(string.lower())})

def test_count_distinct_characters() -> None:
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('") == 0
    assert count_distinct_characters('  ") == 0
    return None
```