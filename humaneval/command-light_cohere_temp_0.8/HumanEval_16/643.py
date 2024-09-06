```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.s.lower() if c in string for c in string})

# Test case
test_string = 'xyzXYZ jerry 123 example'
assert count_distinct_characters(test_string) == 3
```