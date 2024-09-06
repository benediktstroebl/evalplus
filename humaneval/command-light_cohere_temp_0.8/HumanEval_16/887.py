```python
def count_distinct_characters(string: str):
    return len(set(string))

# Test the function
def test_count_distinct():
    assert count_distinct('xyzXYZ') == 3

# Test the function
def test_count_distinct2():
    assert count_distinct('Jerry') == 4
```
This Python script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. It then tests this function using two different test cases to ensure its correctness.