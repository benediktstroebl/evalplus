```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. string()})

def test_count_distinct_characters() -> None:
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('XxvY") == 3
    assert count_distinct_characters('456') == 4
    assert count_distinct_characters(''.join() == 1
    assert count_distinct_characters('hello world') == 8  # Should return 8, with both uppercase and lowercase distinct characters
    return None
```