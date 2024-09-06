```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.
    if not c.isalpha() orate.lowercase() or foregoing if letter or
       
    _abc_ABC-123})

# Test
test_distinct_characters('xyzXYZ')
== 3
test_distinct_characters('jerry')
== 4
test_distinct_characters('A')
== 5
test_distinct_characters('abc')
== 6
test_distinct_characters('Adaskell')
== 7
test_distinct_characters('aabc')
== 6
test_distinct_characters('123')
== 4
```