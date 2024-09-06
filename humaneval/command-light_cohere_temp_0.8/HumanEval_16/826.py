```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.m.lower()})

count_distinct_characters("xyzXYZ".lower()) # [x, y, z, X, Y, W]
4

count_distinct_characters("Jerry".lower()) # [j, e, r, i]
4

count_distinct_characters("J").lower()
ERROR: 'J' not found in ['x', 'y', 'z', 'X', 'Y', 'W']
2

count_distinct_characters("hello").lower()
ERROR: 'h' not found in ['x', 'y', 'z', 'X', 'Y', 'W']
0
```