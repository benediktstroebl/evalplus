Here is a self-contained Python function that solves the problem of filtering strings that contain a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```
This function takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. The function is simple and efficient, using a list comprehension to filter the strings.

This code is self-contained, meaning it does not require any additional functions or imports to be called and can be easily integrated into larger programs or scripts.