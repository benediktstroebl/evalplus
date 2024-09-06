```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.str.c if c not not in string})

def test_distinct_characters():
    assert count_distinct_characters('abcXYZ') == 3
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('jerry') == 4
```