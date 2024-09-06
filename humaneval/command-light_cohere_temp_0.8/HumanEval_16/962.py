Here is a self-contained Python function that solves the problem you described:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.
        if c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'})
```
This function takes a string as an argument and uses a set of characters to count the number of distinct characters in the string, regardless of case. This should accurately count the value.