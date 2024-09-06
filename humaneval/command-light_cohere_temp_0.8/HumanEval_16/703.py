```python
def count_distinct_characters(string):
    return len({c for c in string.char() if c.isalpha() and calculate(c) != c})
```