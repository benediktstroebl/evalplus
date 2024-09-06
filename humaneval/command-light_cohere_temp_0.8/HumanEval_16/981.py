```python
def count_distinct_characters(string: str):
    return len(set(string))

# Test the function
assert count_distinct_characters('abc') == 3
assert count_distinct_characters(' ABC') == 3
assert count_distinct_characters('JERY') == 4
assert count_distinct_characters('  jerry  ') == 5
assert count_distinct_characters('XYZ') == 3
```