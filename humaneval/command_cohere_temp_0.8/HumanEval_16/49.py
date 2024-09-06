Here's a Python script with a self-contained function that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses the `set` function to remove duplicate characters, and the `lower()` method to ensure that both uppercase and lowercase characters are treated the same. It then returns the length of the resulting set, which is the number of distinct characters.