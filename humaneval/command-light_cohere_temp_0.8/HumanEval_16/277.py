```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

#Tests
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('jerry'))    # Output: 4
print(count_distinct_characters('jrrYE'))    # Should return 5)
print(count_distinct_characters(' '))     # Should return 5)
```