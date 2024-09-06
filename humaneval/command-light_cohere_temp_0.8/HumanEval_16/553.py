```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.str.union('') if c in string})

# Unit tests
string1 = "xyzXYZ"
assert count_distinct_characters(string1) == 3

string2 = "jerry"
assert count_distinct_characters(string2) == 4

string3 = "hello123"
assert count_distinct_characters(string3) == 5
```