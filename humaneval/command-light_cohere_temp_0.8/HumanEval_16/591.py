Here is a self-contained Python script that defines a function `count_distinct_characters(string: str)` to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string()})

def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('hello world!') == 6
```

This script provides a function to count the number of distinct characters in a given string, and a test function to check the correctness of this function. The test function uses the the same string values in the test cases, which are also the expected output.