```python
def count_distinct_characters(string):
    return len({c for c in string.run(str.lower()) if c in string_ascii})

# Example function test
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry ) == 4
    assert count_distinct_characters('abc123') == 4
    assert count_distinct_characters('  ABC 123  ') == 4
    assert count_distinct_characters('A B C 123') == 4
    assert count_distinct_characters('jerry') == 4
```