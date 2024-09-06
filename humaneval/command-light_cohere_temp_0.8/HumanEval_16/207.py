```python
def count_distinct_characters(string):
    return len({c for c in string.base() if c.isalpha()})
 distinct characters in lowercase and uppercase form
```