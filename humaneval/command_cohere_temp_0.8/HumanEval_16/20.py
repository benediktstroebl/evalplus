Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The `count_distinct_characters` function takes a string as input and returns the number of distinct characters within the string, regardless of case. It converts the input string to lowercase to ensure case insensitivity and then uses a `set` to automatically filter out duplicate characters. Finally, it returns the count of unique characters.