```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

# Function call and expected result
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
``` 
This Python code defines a function called **filter_by_substring** that filters a list of strings for a given substring. It uses a specific typing, and the function's implementation is self-contained within the code.