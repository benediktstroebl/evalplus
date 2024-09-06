```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.strings() if c not string.isalpha(c)})
```
This function counts the number of distinct characters in the provided string. It uses the strings's built-in method, which is case-insensitive, to create a set of characters in the string and then checks if each character is not a part of that set. This effectively ignores the special characters like numbers and symbols that have special meanings, and only focuses on common alphanumeric characters.