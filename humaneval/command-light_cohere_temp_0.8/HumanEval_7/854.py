```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Tests
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This Python code defines a function called **filter_by_substring** that filters a list of strings for a given substring. The function uses a string method **in** to check if each string contains the given substring. The test section demonstrates the use of the function with a sample input and a specific substring, and the expected output is printed.