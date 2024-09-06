```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not set()})

# Test cases
string1 = 'xyzXYZ'
assert count_distinct_characters(string1) == 3

string2 = 'jerry'
assert count_distinct_characters(string2) == 4

```