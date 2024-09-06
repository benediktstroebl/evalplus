```python
def count_distinct_characters(string):
    return len(set(string.lower()))

string = 'xyzXYZ jerry'
assert count_distinct_characters(string) == 3, "Should have 3 distinct characters"
string = 'jerry Jerry'
assert count_distinct_characters(string) == 4, "Should have 4 distinct characters"
```