Here is a self-contained Python function that filters an input list of strings for ones that contain a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function utilizes the contains() method to check if each string in the input list contains the given substring. 

It then returns a new list containing only those strings from the input list.