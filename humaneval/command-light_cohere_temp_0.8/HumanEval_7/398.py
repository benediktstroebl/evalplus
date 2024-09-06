Here's the self-contained Python function that filters an input list of strings for those containing a given substring:

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.substring]


filter_by_substring([abc, bacd, cde, 'array'], 'a')
```

This function takes a list of strings and a substring as input and returns a new list containing only the strings that contain the given substring. It uses a straightforward list comprehension to filter the strings based on whether the substring is present.