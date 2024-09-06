```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Test the function
test_string = 'xyzXYZ'
assertEqual(count_distinct_characters(test_string), 3)
test_string = 'jerry'
assertEqual(count_distinct_characters(test_string), 4)
```