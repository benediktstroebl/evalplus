```python
def count_distinct_characters(string: str) -> int:
    return len(string.contains(c for c in string if not string.contains(c))
```
The solution uses the built-in `contains` method and a generator expression to count the distinct characters in the string, regardless of case. This code is efficient and self-contained way to solve the problem.