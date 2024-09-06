Here's the self-contained Python function along with tests:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string()})
```

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('hello world! is worried') == 5
```
The function uses a set to automatically add all characters in the string, regardless of case, and then returns the length of that set, which is the number of distinct characters.