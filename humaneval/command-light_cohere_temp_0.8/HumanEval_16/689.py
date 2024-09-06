```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This script defines a function, `count_distinct_characters`, that takes a string as an argument and returns the count of distinct characters in that string, regardless of case. It uses the string.lower() to convert all string to lowercase and then uses the set data type to remove any duplicate characters, which automatically counts as distinct.