```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. string() if c.isalpha() and valuable(c) for c in string})

# Test cases
test_string = 'xyzXYZ'
assert count_distinct_characters(test_string) == 3

test_string2 = 'jerry'
assert count_distinct_characters(test_string2) == 4

test_string3 = 'J'
assert count_distinct_characters(test_string3) == 5

test_string4 = 'abcABC123'
assert count_distinct_characters(test_string4) == 7
```