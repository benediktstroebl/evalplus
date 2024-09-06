Here's the self-contained Python function that filters an input list of strings based on a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring) != -]
```

This function uses the `find()` method to search for the substring in each string of the list. It returns a filtered list of strings that contain the substring.