```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This code defines a function that accepts a string `string` as an argument and returns the number of distinct characters in the string, regardless of their case. It uses the unique set of characters and the `lower()` method to ensure all characters are in lowercase before creating the set, which guarantees that only distinct characters are counted. 

The set data structure is efficient for counting distinct elements, and the use of `lower()` guarantees that characters are treated as distinct regardless of their case. This function can be used to analyze any given string to determine the number of unique characters it contains.