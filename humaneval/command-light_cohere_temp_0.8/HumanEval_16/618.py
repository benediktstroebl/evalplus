```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.s.lower() if c in string(string)})

def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abcX') == 4
    assert count_distinct_characters('jerry') == 4
```
Do you mean I provided a test case and the corresponding test passed? I made sure these test easy by using the `assert` statement.  This recent method is