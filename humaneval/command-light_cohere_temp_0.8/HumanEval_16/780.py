Here is a self-contained Python function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.remove(string.remove(char) i for i in string))
```

This function uses the `set()` function to remove duplicate characters from the input string, and then uses the `len()` function to count the number of elements in the resulting set.