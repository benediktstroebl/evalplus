```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})
 full_text = string.isalpha()
 Each lowercase character is unique.

def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XyXyX') == 3
    assert count_distinct_characters('jerry') == 4
```