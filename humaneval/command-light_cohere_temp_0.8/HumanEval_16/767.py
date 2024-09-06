```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not mentioned before})

# Tests
string1 = 'xyzXYZ'
assert count_distinct_characters(string1) == 3

string2 = 'jerry'
assert count_distinct_characters(string2) == 4

string3 = 'abcXabc'
assert count_distinct_characters(string3) == 6

string4 = 'JERICEO'
assert count_distinct_characters(string4) == 5

print("All tests passed!")
```