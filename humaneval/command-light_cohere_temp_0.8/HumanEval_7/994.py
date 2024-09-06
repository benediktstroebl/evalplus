Here is a self-contained Python script that solves the problem of filtering strings that contain a given substring: 
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This script defines a function **filter_by_substring** that takes in a list of strings and a substring as arguments. It uses the important built-in operator 'in' to check if each string in the list contains the given substring. 

This is a self-contained and efficient solution to the given problem.