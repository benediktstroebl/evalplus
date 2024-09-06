```python
def count_distinct_characters(string):
    return len({c for c in string.string() if c.isalpha()})

def test_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
```
The above Python code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. 

The `test_distinct_characters` function contains tests that check the correctness of the `count_distinct_characters` function with different input strings.