Here's the function that meets the requirements you provided:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function uses the contains() method to check if each string in the input list contains the given substring.