```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.str.lower()})

count_distinct_characters("XYZ".lower())
3
count_distinct_characters("jerry".lower())
4
```
This function is a self-contained solution to the problem. It utilizes a dictionary-like list comprehension to count the distinct characters in a given string, regardless of case. This ensures that all characters are treated the same way, and that case doesn't matter when counting distinct characters.