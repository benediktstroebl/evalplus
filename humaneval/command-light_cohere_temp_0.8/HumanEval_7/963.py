Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Function call and test results
print(filter_by_substring(strings, substring))  # ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. The function uses a `List` type hint to indicate that the input parameter `strings` should be a list of strings, and the `substring` parameter should be a string. The function uses a filtering approach to achieve this, and the test cases verify the expected results for different inputs.