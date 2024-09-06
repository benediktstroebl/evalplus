```python
def count_distinct_characters(string: str):
    return len(set(string.lower()))
```
This function uses the set data structure and the lower() method to convert all characters in the string to lowercase to ensure uniqueness and then counts the number of distinct characters.