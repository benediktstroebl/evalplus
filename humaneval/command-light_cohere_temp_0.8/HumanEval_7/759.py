```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Function call and test results
print(filter_by_substring(strings, substring))  # ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that filters an input list of strings and returns a new list containing only the strings that contain the given substring. The test cases pass successfully, demonstrating the functionality of the function.