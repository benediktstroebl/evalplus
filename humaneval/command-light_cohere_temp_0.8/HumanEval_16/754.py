```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})
 distinct character count

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('JoEY') == 4
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('abcXyzABCD') == 6
    assert count_distinct_characters(' Jerry ') == 4 # test case with spaces
    assert count_distinct_characters('   Jerry   ') == 4 # test case with spaces and newline characters

print(test_distinct_characters())
```