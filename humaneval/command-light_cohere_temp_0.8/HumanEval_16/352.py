```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.char.count(c,case})
   

def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('ABC') == 3
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
```
The function `count_distinct_characters` computes the count of unique characters (case-insensitive) in the given string. It utilizes a also list comprehension and the `count()` function to achieve this. The test function verifies that the function correctly by asserting the outputs against different input strings.