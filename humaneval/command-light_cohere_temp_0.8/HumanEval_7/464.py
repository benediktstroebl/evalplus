```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Function call and expected result
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that filters a list of strings for a given substring. The test cases demonstrate the each input, and the function is called with the test cases and the expected output is printed.