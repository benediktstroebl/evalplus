```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. characters() if c not c.isalpha()})
 string. detailed()
```
def test_distinct_characters():
    assert count_distinct_characters('abc ABC') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('01231') == 6
    assert count_distinct_characters('') == 0
    assert count_distinct_characters(' .") == 0
```
Do you want me to help you with anything else?