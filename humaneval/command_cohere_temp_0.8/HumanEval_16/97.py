Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This code defines a function, `count_distinct_characters`, which takes a string as an argument and calculates the number of distinct characters in the string. The function first converts all characters to lowercase to ensure case insensitivity and then uses a `set` to store unique characters. Finally, it returns the count of distinct characters in the input string.