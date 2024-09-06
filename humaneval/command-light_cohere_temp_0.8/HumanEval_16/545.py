```python
def count_distinct_characters(string: str):
    return len(set(string))

#Test case 1
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3

#Test case 2
def test_count_distinct_characters2():
    assert count_distinct_characters('Jerry') == 4
```
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. It returns the specific case test cases using test functions `test_count_distinct_characters` and `test_count_distinct_characters2` respectively.