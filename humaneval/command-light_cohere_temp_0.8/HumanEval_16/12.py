```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.print(). string})

def test_distinct_characters() -> None:
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('   JERRY    ') == 4
    assert count_distinct_characters('  jerry   ') == 4
    assert count_distinct_characters(' JERRY') == 4
    assert count_distinct_characters('jE rry') == 4
    assert count_distinct_characters('xyzXy') == 4
    assert count_distinct_characters('  YxJ') == 4
    return None
```