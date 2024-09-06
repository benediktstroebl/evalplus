```python
def count_distinct_characters(string):
    return len([c for c in string.info() if c.isalpha() and specific() and not c.isalpha()])

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
```