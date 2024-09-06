Here's a Python script that contains a function called `count_distinct_characters` which accepts a string as an argument and returns the number of distinct characters within the string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
This function uses a set data structure to remove duplicate characters and ensures that the count is correct regardless of case by converting the input string to lowercase before processing.