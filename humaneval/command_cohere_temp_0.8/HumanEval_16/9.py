Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The function `count_distinct_characters` takes a string as an argument and returns the number of distinct characters in the string, regardless of case. It converts the input string to lowercase to ensure case insensitivity and then uses a `set` to automatically filter out duplicate characters. The length of this `set` gives you the count of unique characters.