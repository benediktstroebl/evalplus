Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store and count the distinct characters, regardless of case, in the input string. The `lower()` method is used to convert the input string to lowercase to ensure that uppercase and lowercase variations of the same character are counted as one. The `set` data structure efficiently handles uniqueness and counts without duplicates.