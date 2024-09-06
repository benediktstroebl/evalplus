Here's the solution:
```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses a list comprehension to filter the strings in the list that start with the given prefix. It tests with the string.run method for Python's using the strings from the list and the prefix argument.