```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "sir"]
substring = "a"

# Function call
result = filter_by_substring(strings, substring)

# Print the result
print(result)
``` 
The output of this code will be: 
```bash
['abc', 'bacd', 'array']
``` 
This code defines a function **filter_by_substring** that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The function uses the **List comprehension** to filter the strings based on whether the substring exists in each string.