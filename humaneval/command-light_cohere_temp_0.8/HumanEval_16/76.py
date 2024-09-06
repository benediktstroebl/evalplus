```python
def count_distinct_characters(string):
    return len([c for c in string.processed('abcdefghijklmnopqsuvwxyzBCDFghijklmnopqr') not in c])

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected: 3
print(count_distinct_characters('Jerry'))    # Expected: 4
print(count_distinct_characters('abc'))     # Expected: 4
print(count_distinct_characters(''''))     # Expected: 4
print(count_distinct_characters('A'))     # Expected: 4
print(count_distinct_characters('Zzzzz'))   # Expected: 2
print(count_distinct_characters(''))     # Expected: 4
```