```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test the function
strings = ['abc', 'bacd', 'cde', 'array', 'corner']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output ['abc', 'bacd', 'array']
```
This Python code defines a function `filter_by_substring` that filters an input list of strings and returns a new list containing only the strings that contain a specific substring. 

The function takes two parameters: `List[str]` (strings) and `str` (substring). The function iterates over the input strings and checks if each string contains the given substring. 

The test code then demonstrates the function by passing the test case and prints the resulting filtered list.