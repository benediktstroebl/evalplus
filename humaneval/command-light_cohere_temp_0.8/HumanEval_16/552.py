```python
def count_distinct_characters(string: str):
    return len({c for c in string.string() if c not c.isupper(string)})
```
This function calculates the number of distinct characters in the provided string, regardless of case, using a set of characters and the `isupper` method. The test cases demonstrate the value of the function.