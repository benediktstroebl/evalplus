```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Tests
string1 = 'xyzXYZ'
assert count_distinct_characters(string1) == 3

string2 = 'jerry'
assert count_distinct_characters(string2) == 4

# String with extra whitespace
string3 = '  abc def g  ' h'
assert count_distinct_characters(string3) == 6

# Invalid input
try:
    string4 = '123'
except TypeError:
    assert count_distinct_characters(string4) == 0  # Should raise error
```