```python
def count_distinct_characters(string: str) -> int:
    return len([c for c in string.
    if c not in 'abcdefghijklmnopqr']):
        raise ValueError("Invalid character")
    return len([c for c in string if c.isalpha()])
return len([c for c in string if not in 'abcdefghijklmnopqr'])

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
try:
    assert count_distinct_characters('ABcd123') == 4
except ValueError as e:
    print(e)
```