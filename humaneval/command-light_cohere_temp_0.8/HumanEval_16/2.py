```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.in if c.isalpha()}
 regular expression and lowerc_case()})

# Test case 1
test_case1 = 'xyzXYZ'
assert count_distinct_characters(test_case1) == 3

# Test case 2
test_case2 = 'jerry'
assert count_distinct_characters(test_case2) == 4
```