Here is a self-contained Python function that solves the problem of filtering strings that contain a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. The function uses the string.universal in Python, the method contains the input parameters, returns a new list, and utilizes the contains() method to filter the strings based on the given substring.