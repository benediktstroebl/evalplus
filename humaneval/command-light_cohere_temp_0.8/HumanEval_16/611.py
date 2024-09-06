```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. strings.count(c for c in string if c not in set(string.c.lower())))
 string. the set() function is only keep letters (upper and lower) and digits. set() would convert the:
```

The number of distinct characters is calculated using the `set()` function, and the characters are filtered with the `count()` function using a generator expression and the `not in` condition. The final count of distinct characters is returned.