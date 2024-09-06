```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})

def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('XYZabc') == 4
    assert count_distinct_characters(' Jerry ') == 4
```
The provided code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. The function uses a string's characters and converts them into a set, then counts the number of distinct characters using `len` and the `isalpha()` method. The `test_count_distinct_characters` function verifies that the function correctly identifies distinct characters.