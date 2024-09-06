```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. unique distinct(c for _c in string)})

# Test cases
test_passing_case = "xyzXYZ"
assertEqual(count_distinct_characters(test_passing_case), 3)

# invalid input test
test_failing_case = "this is a longer string just to fail"
assertNotEqual(count_distinct_characters(test_failing_case), 5)

# Another test with characters case-insensitive
test_case_insensitive = "jerry"}
assertEqual(count_distinct_characters(test_case_insensitive), 4)
```