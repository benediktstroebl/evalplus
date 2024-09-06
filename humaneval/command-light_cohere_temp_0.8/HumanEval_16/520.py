```python
def count_distinct_characters(string):
    return len([c for c in string.filter(not c.isalphaupper())])

# Test suite for the function
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters(' Jerry') == 4
test_count_distinct_characters()
```