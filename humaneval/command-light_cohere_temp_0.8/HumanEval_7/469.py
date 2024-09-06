Here's a self-contained Python function that filters an input list of strings based on a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function uses the `contains()` method to check if each string in the input list contains the given substring.  It takes `filter_by_substring()` function is designed to be self-contained and solve the problem of filtering strings that contain a specific substring.