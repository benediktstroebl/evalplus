```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

def test_count_distinct():
    assert count_distinct('abc') == 3
assert count_distinct('XYZ') == 3
assert count_distinct('jerry') == 4

print("All tests passed!")
```