Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to filter out all duplicate characters and then counts the number of distinct characters in the string. The trick to ensuring that this problem is case insensitive is to convert the characters in the string to lowercase using the `lower()` method on the string. This way, 'x' and 'X' are considered the same character.