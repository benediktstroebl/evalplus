```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.language.lower() if c in string})
```.

def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('ABC') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters(' jerry ') == 4
```
The above code defines a `count_distinct_characters` function that calculates the count of distinct characters in a given string, regardless of case. It also provides a test_count_distinct_characters function with assertions to ensure the correctness of the `count_distinct_characters` function.