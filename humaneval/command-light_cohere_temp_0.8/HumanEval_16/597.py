```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test suite for the function
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('JER') == 4
    assert count_distinct_characters('  jerry  ') == 4
    assert count_distinct_characters(''jerry') == 4
```  This script defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string. The test suite ensures the results of the function for various inputs.