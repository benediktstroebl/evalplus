Here's the self-contained Python function:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The function uses the contains() method to check if each string in the input list contains the given substring. It uses list comprehension to create a new list with the matching strings.