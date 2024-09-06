```python
def count_distinct_characters(string: str) -> int:
    return len(string)

# Test cases
string1 = 'abc123'
string2 = 'xyzXYZ'
string3 = 'JERRY'

assert count_distinct_characters(string1) == 3
assert count_distinct_characters(string2) == 4
assert count_distinct_characters(string3) == 4 

print("All tests passed!")
```