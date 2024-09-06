Below is a self-contained Python function that filters an input list of strings for those containing a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function iterates through the input list of strings and returns a new list containing only the strings that contain the given substring. 
The containing condition is implemented using the contains() method of the string class, which returns True if the given string is a substring of the original string.