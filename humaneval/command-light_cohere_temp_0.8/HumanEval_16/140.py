```python
def count_distinct_characters(string: str) -> int:
    return len([char for char in string. distinct_case(char)])

def test_distinct_characters():
    assert count_distinct_characters('abc ABC') == 3
    assert count_distinct_characters('xy Xy') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('  jerry  ') == 4
    assert count_distinct_characters('veryVeryVary') == 4
```
This code provides a function `count_distinct_characters` that calculates the count of distinct characters in a given string. The `test_distinct_characters` function serves to verify the correctness of this function's behavior.