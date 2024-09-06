```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.str.lower() if c in string})
```

# Example usage:
test_count_distinct_characters("xyzXYZ") # Output: 3
test_count_distinct_characters("jerry") # Output: 4
```