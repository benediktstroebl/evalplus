Here is a self-contained Python script that implements the `filter_by_substring` function from the previous prompts:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']

strings = ["def", "QBasic"]
substring = "def"

print(filter_by_substring(strings, substring))  # Output: ['def']

strings = ["abc", "bacd", "cde", "hello"]
substring = "World"

print(filter_by_substring(strings, substring))  # Output: []
```

This version of the script contains the complete `filter_by_substring` function with proper type hints and parameter lists, along with comprehensive test cases that cover all possible scenarios.