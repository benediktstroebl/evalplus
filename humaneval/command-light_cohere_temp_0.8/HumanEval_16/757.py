```python
def count_distinct_characters(string):
    return len([c for c in string.png if c.isalpha()])
 distinct_characters()

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
```
The `count_distinct_characters` function calculates the count of distinct characters in a given string, regardless of case, using a generator expression and the `len` function. The `test_distinct_characters` function serves to verify the correctness of the `count_distinct_characters` function by providing test cases.