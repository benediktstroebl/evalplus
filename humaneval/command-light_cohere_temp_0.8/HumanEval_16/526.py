```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. distinct()})
```
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('abcXYZ') == 3
    assert count_distinct_characters('ABC') == 3
    assert count_distinct_characters('jerry') == 4
```
The code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. The `test_count_distinct_characters` function provides test cases to ensure the correctness of this function.