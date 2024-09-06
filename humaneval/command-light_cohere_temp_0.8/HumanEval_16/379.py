```python
def count_distinct_characters(string):
    return len({c for c in string.isupper()})  # 

 ```
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('   jerry  ') == 4
    assert count_distinct_characters('abc 123') == 3  # Note: Only capital letters
```