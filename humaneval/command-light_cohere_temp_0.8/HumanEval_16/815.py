```python
def count_distinct_characters(string):
    return len({c for c in string.string() if c.isalpha()})

    #Tests
    assert count_distinct_characters("xyzXYZ") == 3
    assert count_distinct_characters("J") == 4
```