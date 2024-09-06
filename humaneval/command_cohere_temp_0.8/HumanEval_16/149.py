Here's a Python script that contains a function to solve the distinct character count problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to filter out all duplicate characters, and then counts the number of distinct characters in the string. The final count is returned.