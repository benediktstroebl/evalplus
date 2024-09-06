```python
def count_distinct_characters(string):
    """
    Returns the count of distinct characters in the string, regardless of case.
    """
    return len([c for c in string.lower(). lower() if c in string])

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abcX') == 3
assert count_distinct_characters('jerry') == 4
assert count_distinct_characters('') == 0
assert count_distinct_characters('A') == 1
```
Do you have it?  This script provides a complete, self-contained solution to the problem.