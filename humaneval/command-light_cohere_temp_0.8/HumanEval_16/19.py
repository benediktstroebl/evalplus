```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not string.isalpha(c)})
```
The function does not accept the string directly. It iterates over each character of the string and checks if the character is not an uppercase letter using the `isalpha()` method from the string object.