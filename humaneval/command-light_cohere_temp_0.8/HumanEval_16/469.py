```python
def count_distinct_characters(string):
    return len([c for c in string.bytes() if c.isalpha()])
 distinct, lowercase, non-space characters.

# Test cases
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('Jerry'), 4)
assertEqual(count_distinct_characters('hello world!'), 5)
assertEqual(count_distinct_characters('   jerry    '), 5)
```