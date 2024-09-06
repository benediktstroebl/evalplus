```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not set()})
```

The function takes a string as input and uses the set() method with a generator expression to create an empty set. It then iterates over each character in the string, and for each character, it checks if it's not already in the set. This ensures that only distinct characters are kept in the set, effectively counting the number of distinct characters.