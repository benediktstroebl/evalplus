Here's the improved code:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string(). specific to lower case for c in string})

def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('  jerry  ') == 4 # Should be 4
    assert count_distinct_characters('abc') == 3    # Should be 3

```
This version offers a more descriptive function name and incorporates the test cases as specified. It also ensures proper indentation and formatting for better readability.