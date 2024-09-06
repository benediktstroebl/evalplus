Here's a self-contained Python function that filters an input list of strings based on their prefix:
```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the given prefix. The function utilizes the specific to check if the given string starts with the given prefix.