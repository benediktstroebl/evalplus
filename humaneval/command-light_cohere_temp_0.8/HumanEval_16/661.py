```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()}
 than c.isalpha()))

def test_distinct_characters(string: str) -> None:
    assert count_distinct_characters('abc').equals(3), "should return 3")
    assert count_distinct_characters('jerry').equals(4), "should return 4")
```