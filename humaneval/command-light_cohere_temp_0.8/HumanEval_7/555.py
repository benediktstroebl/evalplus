```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

strings = ["pqr", "python", "code", "github"]
substring = "go"

result = filter_by_substring(strings, substring)
print(result)  # Output: []
``` 
This code defines a function called `filter_by_substring` that filters a list of strings based on whether the given substring exists within each string. It uses the
 List comprehension to achieve this. The test cases demonstrate the strings are filtered successfully.