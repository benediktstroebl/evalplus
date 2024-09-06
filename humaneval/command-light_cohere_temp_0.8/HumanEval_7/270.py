Here's the improved Python script with a self-contained function that filters an input list of strings for those containing a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The provided Python script defines a function called **filter_by_substring** that takes a list of strings and a substring as input. It utilizes the strings. The list comprehension technique to filter and return a new list containing only the strings from the input list that contain the given substring. This script is provides a self-contained solution to the problem of filtering strings based on a substring.