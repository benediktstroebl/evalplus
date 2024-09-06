```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. characters() if c not neck and c in string})

def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('bb') == 2
    assert count_distinct_characters('  jerry  ') == 3
    assert count_distinct_characters('abcXyz') == 3

print("Passed all tests!")
```