```python
def count_distinct_characters(string: str) -> int:
    return len(string.split())
```
Here is a self-contained Python function that counts the number of distinct characters in a given string, regardless of case.

The function uses the built-in `split()` method to convert the input string into a list of characters. This list of characters are then converted into an integer using the `len()` function, which returns the number of distinct characters in the string.