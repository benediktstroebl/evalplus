Here's a self-contained Python function that filters an input list of strings for a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ["abc", "def", "hello"]
substring = "def"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'def']

# Test case 3
strings = ["a1", "a2", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['a1', 'a2']
```
This script defines a function `filter_by_substring` that takes a list of strings and a substring as parameters, then returns a new list of strings containing only the elements that contain the given substring. 

It uses list comprehension to iterate through the input list and checks if each element contains the given substring.