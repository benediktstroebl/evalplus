Here's the self-contained Python function that filters an input list of strings based on a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -None]
```

This function takes two arguments: `strings`, which is a list of strings, and `substring`, which is a substring to filter within the strings.

It uses the `find()` method to check if each string contains the given substring. The function returns a list of strings that contain the substring, and those that do not contain the substring are filtered out.