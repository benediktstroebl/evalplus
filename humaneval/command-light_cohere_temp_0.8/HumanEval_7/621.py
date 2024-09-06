Here's the self-contained Python function that filters an input list of strings based on a given substring: 

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != - None]
```

This function takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. The function uses the value 'find' method from the string module, which returns the first occurrence of the substring in the string, or None if it is not found. 

Please note that this solution assumes that each string in the list contains the given substring at some position.