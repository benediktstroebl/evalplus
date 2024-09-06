```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This Python function, `count_distinct_characters`, takes a string as input and returns the count of distinct characters in that string, regardless of case. The distinct characters are obtained using the set of lowercase characters and then counting the number of unique characters. 

This function is self-contained and does not rely on any other functions or modules, making it easy to use and understand. 

The function uses Python's built-in `set` and `len` functions, along with the `lower` method to ensure the characters are treated as distinct regardless of case.