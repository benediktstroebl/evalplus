```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]
# tests
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # ['abc', 'bacd', 'array']
``` 
This function filters a list of strings based on a given substring. It returns a filter of elements that contain the given substring.