Here's the self-contained Python function that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. String.count(c(c), count(c) == 1 for c in string})
```

This function iterates through each character in the input string and counts how many times each character appears. It does not consider case, so the result is the total number of distinct characters in the string, regardless of case.