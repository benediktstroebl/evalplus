```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.22 if c.isalpha()}

``` string
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('JER') == 4

test_distinct_characters()
```