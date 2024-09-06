Here's a Python script with a self-contained function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if string.isalpha(c)})
```

This function iterates through each character in the string and uses a dictionary comprehension to count the number of distinct characters. The function then returns the uniqueness count of the characters in the given string.