```python
def count_distinct_characters(string: str):
    return len({c for c in string. characters() if c.isalpha()})

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry ') == 4
```