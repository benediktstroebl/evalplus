```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.filter(str.isalpha(), True)): 

def test_count_distinct_characters() -> None:
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('great') == 4
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters(' abcdef ghi') == 6
    assert count_distinct_characters('Hi There') == 8
    return None
```