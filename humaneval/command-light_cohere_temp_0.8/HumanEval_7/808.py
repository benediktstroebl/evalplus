```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function
test_list = ["abc", "bacd", "cde", "array", "hello", "world"]
test_substring = "array"

result = filter_by_substring(test_list, test_substring)
print(result)  # Output: ['array']
```
The solution passes the tests, and the function correctly filters the strings that contain the substring.