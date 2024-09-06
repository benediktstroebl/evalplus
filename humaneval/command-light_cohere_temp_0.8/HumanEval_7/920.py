Here's the provided Python code:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Function call and test
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function called **filter_by_substring** that filters a list of strings for a given substring. It uses the read-only and return the elements of the list that contain the substring. The test cases demonstrate the use of the function with different inputs and verify the output matches the expected result.