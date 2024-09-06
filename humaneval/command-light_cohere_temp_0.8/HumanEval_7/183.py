Here's the function `filter_by_substring`, which filters a list of strings based on a given substring:

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function uses the `contains` method to filter the strings in the list that contain the given substring. The function returns a filtering list of strings.