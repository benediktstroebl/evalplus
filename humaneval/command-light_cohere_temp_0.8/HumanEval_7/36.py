```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Expected output: ['abc', 'bacd', 'array']
``` 
This code defines a function **filter_by_substring** that filters a list of strings for a given substring. It uses a use a list comprehension to check if each string in the input list contains the specified substring. This function successfully passes all test case and can be used for real-world scenarios.