```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1
strings = ['abc', 'bacd', 'cde', 'array', 'hello']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ['abc', 'banana', 'carrot', 'hello', 'world']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'banana', 'carrot', 'hello', 'world']

# Test case 3
strings = ['abc', 'def', '123']
substring = '123'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['123']
```
This Python code defines a function `filter_by_substring` that filters an input list of strings based on a given substring. The function iterates through each string from the input list and checks if the substring exists in the string. This effectively filters the the the output of the function is the list of strings that contain the specified substring.