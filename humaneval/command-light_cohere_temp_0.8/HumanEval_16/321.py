```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.str.find(' ', string) })
# split the string into a list of characters and count distinct ones
```
This function takes a string as input and uses the `str.find()` function to split the string into a list of characters. Then, it counts the distinct characters from this list and returns the count.

It uses the ** { ... }.find() ** list comprehension, which creates a new list that contains only the distinct characters from the original list.