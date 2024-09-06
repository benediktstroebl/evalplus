```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3

def test_count_distinct_characters2():
    assert count_distinct_characters('XYZ') == 3

def test_count_distinct_characters3():
    assert count_distinct_characters(' Jerry ') == 4
```