```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string()})
print(count_distinct_characters('xyzXYZ')) #3
print(count_distinct_characters('jerry')) #4
```