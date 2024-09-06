```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()} )
    microcosmic plain text.
# Test Case using the string
count_distinct_characters('xyzXYZ') # [3]
# Test a more complex string
count_distinct_characters('Jerry') # [4]
```