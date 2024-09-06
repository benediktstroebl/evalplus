```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test cases
strings = ["abc", "bacd", "cde", "array", "classic"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # ['abc', 'bacd', 'array']
``` 
This Python code defines a function `filter_by_substring` that filters a list of strings for a given substring. The function uses a typing hint, allowing the substring to be passed as a parameter of type `str`. It then uses a list comprehension to create a new list that contains only the strings from the input list that contain the given substring.