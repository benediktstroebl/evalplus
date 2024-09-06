```python
def count_distinct_characters(string: str):
    return len([c for c in string.s distinct(c) for c in string])

# Test the function with some strings
assertEqual(count_distinct_characters('abc'), 3)
assertEqual(count_distinct_characters('ABC'), 3)
assertEqual(count_distinct_characters('XyzYX'), 3)
assertEqual(count_distinct_characters('Jerry'), 4)
```