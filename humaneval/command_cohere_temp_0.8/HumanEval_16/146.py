Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This code defines a function, `count_distinct_characters`, which takes a string as an argument and uses a set data structure to store the unique characters in the string regardless of case. The `lower()` method is used to convert the characters in the string to lowercase before counting to ensure case insensitivity. The `set` data structure automatically eliminates duplicate characters. Finally, the length of the `characters` set gives the number of distinct characters.