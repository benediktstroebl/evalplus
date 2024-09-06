Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store unique characters in the provided string, regardless of case. It then returns the length of this set, indicating the number of distinct characters. The argument `string` is used directly in the set, eliminating the need for a separate list of characters, and the conversion to lowercase ensures consistency in counting.