```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.read() if c.isalpha()})
 distinct character in the string
def test_distinct_characters():
    assert count_distinct_characters("xyXYZ") == 3
    assert count_distinct_characters("jerry") == 4
```