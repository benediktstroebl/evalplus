```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Function call and test results
print(filter_by_substring(strings, substring))  # ['abc', 'bacd', 'array']

strings = ["abcf", "hello", "hello world"]
substring = "cf"

# Function call and test results
print(filter_by_substring(strings, substring))  # ['abcf']
```

The code defines a function `filter_by_substring` that takes two parameters: a list of strings and a substring. The function returns a filter the list of strings that contain the substring. The test cases demonstrate the the function's ability to filter the strings correctly.