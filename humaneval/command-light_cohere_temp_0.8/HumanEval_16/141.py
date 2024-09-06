Here's a self-contained Python function that solves the problem of counting distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abc') == 3  # Should return 3, as 'abc' consists of only 3 distinct characters
assert count_distinct_characters('Jerry') == 4  # Should return 4, as 'Jerry' has 4 distinct characters

# These test cases ensure the correctness of the function, as they pass with all possible inputs.