```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not c.isupper(string)})
``` 
Here, we use a set-based approach to find all distinct characters in the string. We then remove duplicates using the recommended by 'isupper'.  The function returns the number of distinct characters.  It testing can also pass a simple test.