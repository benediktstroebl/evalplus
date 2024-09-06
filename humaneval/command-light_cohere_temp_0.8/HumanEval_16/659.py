Here is a Python script with a self-contained function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isupper(c)})
```
Do you need help with anything else?