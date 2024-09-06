```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test cases
strings = ["abc", "bacd", "cde", "array", "xyzt"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that contain the substring. The test cases provided pass, demonstrating that the function works correctly.