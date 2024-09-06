Here is a self-contained Python script that defines a function `count_distinct_characters(string: str)` that calculates the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test cases
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('Jerry'), 4)
assertEqual(count_distinct_characters('xyzXYZ jerry'), 6)
assertEqual(count_distinct_characters(''''), 0) # Empty string
assertEqual(count_distinct_characters(' ' abc def'), 3) # Single character
```