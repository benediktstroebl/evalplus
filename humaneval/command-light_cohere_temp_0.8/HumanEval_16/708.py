Here is a self-contained Python script that solves the problem of counting the distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This script defines a function called `count_distinct_characters` that takes a string as input and returns the number of distinct characters in that string, regardless of case. The function uses the unique set difference algorithm to achieve this.