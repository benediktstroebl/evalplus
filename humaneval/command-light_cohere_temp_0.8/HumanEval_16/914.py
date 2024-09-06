```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.all()))

# Unit tests for the function
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('Jjerry') == 4
```
The test_count_distinct_characters function tests the count_distinct_characters function with various inputs, ensuring the results are as expected.  This expected output is 3 for 'xyzXYZ', 3 for 'abc', and 4 for 'Jjerry'.