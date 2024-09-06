```python
def count_distinct_characters(string):
    return len({c for c in string.md_lower if c != c.isalpha()})
 unique characters and digits, regardless of case
```