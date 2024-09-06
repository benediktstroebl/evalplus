```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.keys() if c.isupper()})

def test_distinct_characters() -> None:
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('JERRY') == 4
    assert count_distinct_characters(' abc 123 ') == 5
    assert count_distinct_characters(' ') == 1
    assert count_distinct_characters(' assisted coders') == 5
    assert count_distinct_characters('  Assisted  Coders  ') == 5
    assert count_distinct_characters(' assisted  CODERS') == 6
    return None  # Lots of test cases, don't want to expose the rest of the function
```