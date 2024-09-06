Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This script defines a function `count_distinct_characters` which takes a string as an argument and returns the number of distinct characters within the string, regardless of case. It converts the input string to lowercase to ensure case insensitivity and then uses a `set` to automatically filter out duplicate characters. Finally, it returns the length of this set, which is the count of distinct characters.