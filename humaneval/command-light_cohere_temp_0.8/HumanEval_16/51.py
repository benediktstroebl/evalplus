```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Tests
string1 = 'xyzXYZ'
assert count_distinct_characters(string1) == 3

string2 = 'jerry'
assert count_distinct_characters(string2) == 4

string3 = 'abcdefghijklmnopqr'
assert count_distinct_characters(string3) == 13

string4 = 'a'
assert count_distinct_characters(string4) == 1
```