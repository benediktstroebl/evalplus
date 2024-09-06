```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('JERRY') == 4

if __name__ == "__main__":
    test_count_distinct_characters()
 ```
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. The function uses the optimized set membership to count distinct characters and passes all tests with the unit test.