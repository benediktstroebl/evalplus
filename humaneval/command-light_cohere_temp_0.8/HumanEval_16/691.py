```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

#Test suite
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters(' abcdefg') == 5
assert count_distinct_characters(' jerry') == 4

if __name__ == "__main__":
    test_count_distinct_characters()
```
This code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. The test suite contains a test cases, which ensure that the function correctly calculates the number of distinct characters. 

This code is self-contained and can be copied and pasted into any Python environment to be used.