```python
def count_distinct_characters(string: str):
    return len([c for c in string.string() if c.isalpha()])

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Toward') == 4

test_distinct_characters()
```