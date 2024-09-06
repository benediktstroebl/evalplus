Here's the self-contained Python function that filters an input list of strings for those containing a given substring:

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function utilizes the contains() method to check if each string in the input list contains the given substring. 

This approach provides a self-contained solution within the function, eliminating the need for explicit input lists and external test cases.