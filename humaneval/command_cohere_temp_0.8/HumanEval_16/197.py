Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to remove duplicate characters and converts the input string to lowercase to ensure case insensitivity. The `len()` function is then used to determine the number of distinct characters.