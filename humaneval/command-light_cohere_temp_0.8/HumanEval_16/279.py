Here's a self-contained Python script that defines a function 'count_distinct_characters' solving the problem of counting distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string()})
```This script provides a straightforward and concise way to find the number of distinct characters in a given string.