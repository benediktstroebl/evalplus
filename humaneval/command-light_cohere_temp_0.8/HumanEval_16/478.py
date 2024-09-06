```python
def count_distinct_characters(string):
    return len({c for c in string.text(lower()) if c not in string.text(''.join())}
```
You can use this function to get the count of distinct characters in any given string.