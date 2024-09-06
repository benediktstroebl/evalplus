```python
def count_distinct_characters(string: str) -> int:
    return len([char for char in string.string() if char not in string.string()])

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('boba') == 4
    assert count_distinct_characters(' test ') == 5
    assert count_distinct_characters('jerry') == 4
```