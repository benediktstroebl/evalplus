Here's a Python script with a self-contained function that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses the `set` function to remove duplicate characters, and the `len` function to count the number of distinct characters, regardless of case, in the input string. As the set is inherently case-sensitive, we use the `lower()` method to convert the entire string to lowercase to ensure an accurate count of distinct characters.