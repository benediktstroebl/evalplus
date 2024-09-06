Here is a self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c not in string. strings()})
```Here is a function that counts the number of distinct characters in a given string. It does this using a `set` to iterate over all characters in the string and `in` to filter out duplicate characters. This function returns the str integer representing the number of distinct characters in the string.