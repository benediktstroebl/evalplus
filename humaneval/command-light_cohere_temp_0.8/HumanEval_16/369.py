```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.case_ins))
```
This function uses the `set()` method along with the `case_insensitive` argument to create a set of all characters in the input string. The `len()` function then returns the count of unique characters in the set, which is also the number of distinct characters in the string, regardless of their case.