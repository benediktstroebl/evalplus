```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. string() if c.isalpha()})
 distinct character count

# Test
test_count_distinct_characters('xyzXYZ')
==> 3
test_count_distinct_characters('Jerry')
==> 4
```