```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. distinct()})
```
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abcX') == 3
    assert count_distinct_characters('jerry') == 4
```
The above Python script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. 

The `test_count_distinct_characters` function contains tests that validate the correct behavior of the `count_distinct_characters` function for various inputs.