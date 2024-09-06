Here's the self-contained Python function that filters an input list of strings for those containing a given substring: 

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The above function filters a list of strings and returns a new list containing only the strings that contain the given substring.