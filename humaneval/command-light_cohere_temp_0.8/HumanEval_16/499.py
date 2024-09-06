```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})
 unique characters in the string
def test_distinct_characters(string):
    assert count_distinct_characters(string) == len({c for c in string.isalpha()}):
```