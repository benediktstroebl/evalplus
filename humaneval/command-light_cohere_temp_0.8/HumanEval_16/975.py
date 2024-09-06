```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()}
 distinct character and not c.isalpha()))
```
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('AbC') == 2
    assert count_distinct_characters('jerry') == 4
```
This test_distinct_characters function tests the count_distinct_characters function with various inputs and checks the results against the expected outputs. The test helps to ensure the correctness of the function.