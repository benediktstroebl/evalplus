```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. strings() if c.isalpha()})
 count = 0
    for c in string:
        if c not in count:
            count += 1
    return count

# Example usage
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4

# Your code is ready!
```