Here's a self-contained Python function that filters an input list of strings for those containing a given substring:

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function uses the contains() method to check if each string in the list contains the given substring.  The expected input is a list of strings and the substring to filter, and the function returns a new list that contains only the strings that contain the substring.