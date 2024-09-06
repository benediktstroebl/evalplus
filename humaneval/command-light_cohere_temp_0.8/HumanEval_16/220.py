```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.value = len(characters))
    return characters.value

def test():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry') == 4
    assert count_distinct_characters('  jerry  ') == 4
    assert count_distinct_characters('a') == 1
    assert count_distinct_characters('abc123') == 3
    assert count_distinct_characters('') == 0
```