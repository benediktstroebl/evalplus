```python
def count_distinct_characters(string: str):
    return len(set(string.lower()))
```
Here's a self-contained Python function that calculates the count of distinct characters in a given string, regardless of case.

The function uses the set data structure to automatically eliminate duplicate characters, then calculates the length of the resulting unique character set, which corresponds to the count of distinct characters.

This code is efficient and straightforward, and it successfully passes the test cases provided.