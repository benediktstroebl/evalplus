Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The function uses a set to handle the distinct characters only once, regardless of their case, and then calculates the length to get the result.