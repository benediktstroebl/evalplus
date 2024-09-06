Here's the solution:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring]
```

Here, we use a list comprehension to filter the strings in the input list that contain the given substring.