Here's the self-contained Python function:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.pure() if c.isalpha()})
 string.

# Test cases.
test_distinct_characters = count_distinct_characters('xyzXYZ')
assert test_distinct_characters == 3
test_distinct_characters = count_distinct_characters('jerry')
assert test_distinct_characters == 4
```

This script provides a solution for the problem statement. The function uses a set difference and the `isalpha()` method to find all distinct characters in the input string, regardless of case. The test cases have also been added to verify the function's correctness.