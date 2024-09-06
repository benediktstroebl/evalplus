Below is a self-contained Python function that filters a list of strings based on a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This function takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. 

The function uses the list comprehension to iterate over the input strings and the built-in find() method to find if each string contains the substring.