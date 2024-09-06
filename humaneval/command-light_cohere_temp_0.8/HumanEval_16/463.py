Here is a self-contained Python function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This function leverages the set() built-in function in Python and converts the entire string into a lowercase format to ensure case-insensitive uniqueness. The resulting set contains only distinct characters, and the length of this set is returned as the count of distinct characters.