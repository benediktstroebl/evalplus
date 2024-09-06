Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The count_distinct_characters function takes a string as input and returns the number of distinct characters within the string, regardless of case. In the code, the input string is converted to lowercase using the `lower()` method to ensure case insensitivity. The characters are then stored in a set, which automatically eliminates duplicate characters, counting them only as single occurrences. The function then returns the length of the set, indicating the number of distinct characters in the input string.