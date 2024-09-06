```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]

 
# Example Test Cases
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
substring = 'a' 

result = filter_by_substring(strings, substring)
print(result)  # Output ['abc', 'bacd', 'array']
```
This Python script defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function uses the method `find()` to search for the substring within each string in the list, and returns the strings that contain the substring.