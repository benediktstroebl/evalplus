```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'adfa']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Expected output: ['abc', 'bacd', 'array']
```
This code defines a function `filter_by_substring` that filters a list of strings and returns a new list containing only the strings that contain a given substring. 
The example demonstrates the usage of the function with a list of strings and a specific substring, and the output is printed to the console.