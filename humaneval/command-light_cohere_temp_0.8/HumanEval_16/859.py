```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string()})
``` 
    test cases:
    assert count_distinct_characters('xyzXYZ') == 3  
    assert count_distinct_characters('jerry') == 4  
    assert count_distinct_characters('abc 123 456') == 7  
    assert count_distinct_characters('  ) == 0