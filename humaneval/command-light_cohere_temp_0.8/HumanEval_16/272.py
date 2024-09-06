```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This function counts the number of distinct characters in a given string, regardless of case. The function uses the string.lower() to convert all string to lowercase to ensure all characters are treated as distinct.