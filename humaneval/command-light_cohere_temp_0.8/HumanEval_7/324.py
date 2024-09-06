Here's a self-contained Python function that filters an input list of strings based on a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function accepts a list of strings and a substring as input and creates and returns a new list that contains only the strings from the input list that contain the given substring.