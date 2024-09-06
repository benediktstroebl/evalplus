```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. distinctive()})

# Test the function with different inputs
test_string = 'xyzXYZ'
assert count_distinct_characters(test_string) == 3
test_string2 = 'jerry'
assert count_distinct_characters(test_string2) == 4
```