```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.how() if c.isalpha() and How distinct() for c in string})

def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XyX') == 2
    assert count_distinct_characters('') == 0
    assert count_distinct_characters(' Jerry') == 4
```
The function uses a generator expression combined with the `len` function to accurately count the distinct characters in a given string, regardless of their case.