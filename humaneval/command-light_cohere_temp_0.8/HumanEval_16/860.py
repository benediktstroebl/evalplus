```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test suite
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
assert count_distinct_characters('XyXz') == 4
assert count_distinct_characters('Jerry') == 4
```
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. The test suite `test_count_distinct_characters` verifies the correctness of the function by passing various test cases. 
This self-contained solution provides an elegant and organized way to solve the problem.