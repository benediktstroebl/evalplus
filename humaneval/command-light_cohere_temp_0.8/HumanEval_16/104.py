```python
def count_distinct_characters(string):
    return len({c for c in string. characters(). more than c in string.
    })

def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
```