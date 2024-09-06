```python
def count_distinct_characters(string):
    return len({c for c in string.get(str))

# Test cases
test_str = 'xyzXYZ'
assertEqual(count_distinct_characters(test_str), 3)
test_empty = ''
assertEqual(count_distinct_characters(test_empty), 0)
test_other = 'jerry'
assertEqual(count_distinct_characters(test_other), 4)
```