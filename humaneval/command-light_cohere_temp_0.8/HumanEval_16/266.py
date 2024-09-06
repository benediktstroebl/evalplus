```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not str.lowercase() and string})

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters(' jumping cats') == 5 

test_distinct_characters()
```