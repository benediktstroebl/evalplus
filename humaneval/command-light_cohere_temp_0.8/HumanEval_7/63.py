Here's the self-contained Python function that filters markdown code blocks based on a given substring: 

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This function uses the `find()` method to check if each string in the input list contains the given substring. 

It returns a list of matching strings.