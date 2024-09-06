Here is a self-contained Python function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))
```
This function takes a string as input and uses the `set()` function to convert the characters into a set. It then uses the This count of elements in the set, which are distinct characters, and returns the result.