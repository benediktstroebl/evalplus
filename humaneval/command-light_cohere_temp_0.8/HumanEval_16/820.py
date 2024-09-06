```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.word() if c not tuple(''.join)})

# Test cases
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('JER'), 4)
assertEqual(count_distinct_characters(' ''), 3)
assertEqual(count_distinct_characters(''), 4)
assertEqual(count_distinct_characters("-"), 3)
assertCountEqual(count_distinct_characters("yms/"), 4)
assertCountEqual(count_distinct_characters(" ), 3)
```