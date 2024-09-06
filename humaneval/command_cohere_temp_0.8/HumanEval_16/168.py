Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The `count_distinct_characters` function takes a string as input and returns the number of distinct characters in the string, regardless of case. In the code, the input string is converted to lowercase using the `lower()` method to ensure case insensitivity. The resulting string is then converted into a set which removes duplicate characters, and its length is returned as the final answer. 

This solution adheres to the problem statement and provides the required functionality in a concise manner.