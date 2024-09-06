```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This Python function, `count_distinct_characters`, takes a string as input and returns the count of distinct characters in that string, regardless of case. Using the `set()` function with a lowercase string is a way to get all distinct characters in a string. The function uses the string passed to the `set()` function and the `len()` function to count the number of elements in the resulting set.