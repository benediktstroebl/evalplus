```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. characters() if c.isalpha()})
 count = len({c for c in string if c.isalpha()})
    count
    distinct_count
def test_distinct_characters(string):
    return count_distinct_characters(string) == len({c for c in string if c.isalpha()})
```