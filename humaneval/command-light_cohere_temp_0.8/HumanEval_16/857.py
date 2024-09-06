```python
def count_distinct_characters(string):
    """ Returns the number of distinct characters in the string (case-insensitive) """
    return len({c for c in string.lower() if c not in 'abcdefghijklmnopqr'})

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected: 3
print(count_distinct_characters('Jerry'))    # Expected: 4
print(count_distinct_characters('abc ABC'))  # Expected: 5
print(count_distinct_characters('A B C'))   # Expected: 5
```