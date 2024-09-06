Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, regardless of case. It first converts the input string to lowercase and then uses the `set()` method to remove any duplicate characters and store them as a set. Finally, the `len()` function retrieves the count of distinct characters in the set.