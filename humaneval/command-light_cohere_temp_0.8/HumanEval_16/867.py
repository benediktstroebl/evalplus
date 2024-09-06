```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.
    if c.isalpha()})
 distinct
    return
def test_distinct_count(test_string):
    assert count_distinct_characters(test_string) == len(test_string)
    return
```