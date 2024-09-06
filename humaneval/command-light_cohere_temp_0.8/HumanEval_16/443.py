```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not c.isalpha() and strings,
        char))

#Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('abcABC') == 3
    assert count_distinct_characters('123XYZ') == 3
    assert count_distinct_characters('a') == 1
    assert count_distinct_characters('12') == 2
    
#Main function usage
print(count_distinct_characters('abcABC'))
 ```