Here's the self-contained Python function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.remove(str.strip, "")))
```
This function removes any non-alphphanumeric characters from a string and then uses the `len()` function to get the length of the resulting set, which contains only the distinct characters. The function then returns the string length, which is the number of distinct characters in the original string.