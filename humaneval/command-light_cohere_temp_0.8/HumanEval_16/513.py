```python
def count_distinct_characters(string: str):
    return len({c for c in string. distinctive()})
# Tests
test_distinct_characters("xyzXYZ") # [x, y, z, X, Y, ] should return 3
test_distinct_characters("Jerry") # [J, e, y, ] should return 4
```