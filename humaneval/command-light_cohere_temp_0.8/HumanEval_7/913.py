```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case: filtering strings containing 'a'
test_case = ["abc", "bacd", "cde", "array"]
substring = "a"
result = filter_by_substring(test_case, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The test case demonstrates the also how the function can filter and retrieve strings that contain a specific substring.