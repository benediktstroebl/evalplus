```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring]
```

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
sub = "a"

result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function **filter_by_substring** that filters an input list of strings and returns a new list containing only the strings that contain the given substring. 

This function uses the **List comprehension** to filter out the strings that do not contain the specified substring.