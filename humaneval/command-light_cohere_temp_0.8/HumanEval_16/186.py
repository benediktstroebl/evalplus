```python
def count_distinct_characters(string):
    return len([c for c in string.values(str.lower()) if c != ''])

# Test suite for function
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abcXyz') == 3
    assert count_distinct_characters('jerry') == 4
```
This code defines a function that calculates the count of distinct characters in a given string, regardless of case. The test suite ensures that the function behaves correctly for various inputs.