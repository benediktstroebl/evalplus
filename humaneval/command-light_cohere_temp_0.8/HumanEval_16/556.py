```python
def count_distinct_characters(string):
    return len({c for c in string.string() if c not in string.}


def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry ') == 4
    assert count_distinct_characters('  hello world   ') == 7
    assert count_distinct_characters('hello world! wtf all right! 'different') == 3
```