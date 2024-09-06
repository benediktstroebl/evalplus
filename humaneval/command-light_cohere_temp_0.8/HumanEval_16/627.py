```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Test cases
string1 = "xyzXYZ"
assert count_distinct_characters(string1) == 3
string2 = "jerry"
assert count_distinct_characters(string2) == 4
```