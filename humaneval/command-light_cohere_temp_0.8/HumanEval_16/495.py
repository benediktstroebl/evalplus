```python
def count_distinct_characters(string: str) -> int:
    """
    Count distinct characters, ignoring case.
    """
    return len(set(string.lower()))
```
# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('jerry'))  # Output: 4
```
Do you require any further assistance with writing code or have a different question?