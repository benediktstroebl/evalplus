Here's a self-contained Python function that filters an input list of strings for a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. It uses the
 List comprehension to iterate over the input list and the substring, and checks if each string contains the substring using the contains() method.