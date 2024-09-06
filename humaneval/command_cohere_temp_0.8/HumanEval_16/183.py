Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The `count_distinct_characters` function takes a string as input and calculates the number of distinct characters in the string. It converts each character in the string to lowercase using the `lower()` method to make the counting case-insensitive and then uses the `set()` function to put all characters into a set, which automatically removes duplicate characters. Finally, the function returns the number of distinct characters in the set.