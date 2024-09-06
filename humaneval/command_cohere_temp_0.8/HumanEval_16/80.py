Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set data structure to remove duplicate characters and optimally count distinct characters. The `lower()` method is applied to convert all characters in the string to lowercase before feeding them into the set, ensuring that uppercase and lowercase variations of the same character are counted as one.