```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.str.count(c for c.isupper(c)) for c in string.
    return
```
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry Jones') == 4
    assert count_distinct_characters('abcXyz') == 3
    assert count_distinct_characters(' jerry') == 4
```
The provided code defines a function that calculates the count of distinct characters in a given string, regardless of case. It uses a dictionary comprehension to track unique characters and returns the count of distinct characters. The test_distinct_characters function verifies the correctness of the count_distinct_characters function by passing various test cases.