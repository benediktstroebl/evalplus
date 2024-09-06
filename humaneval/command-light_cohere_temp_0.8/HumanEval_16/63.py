```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.static()})
```
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
```
Do you want me to help you with anything else related to coding or provide assistance with another topic?