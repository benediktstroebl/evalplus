Here's the solution:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})
 basic implementation that ignores lowercase and counts distinct characters only once.