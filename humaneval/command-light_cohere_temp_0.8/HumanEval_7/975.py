Here's a self-contained Python function that filters an input list of strings for those containing a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function takes two parameters: a list of strings and a substring. It uses the string.contains() method to check if each string in the list contains the given substring. 

The function then returns a new list containing only those strings that contain the given substring. 

This function is self-contained and effectively solves the problem of filtering strings for those containing a given substring.