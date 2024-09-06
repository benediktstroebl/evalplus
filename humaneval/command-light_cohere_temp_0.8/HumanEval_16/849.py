```python
def count_distinct_characters(string):
    return len({c for c in string.string() if c.isalpha()})
 distinct_char_count = len(set(string))
    return distinct_char_count

# Test cases
print(count_distinct_characters('xyzXYZ'))
# This will print 3, since there are 3 distinct characters.

print(count_distinct_characters('Jerry'))
# This will print 4, since there are 4 distinct characters in the string.
```